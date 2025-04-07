from flask import Flask, request, jsonify
from security.input_validator import sanitize_input
from security.auth import require_api_key
from security.logger import log_request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address, default_limits=["10 per minute"])

@app.before_request
def before_request():
    log_request(request)

@app.route('/chat', methods=['POST'])
@require_api_key
@limiter.limit("5 per minute")
def chat():
    data = request.get_json() or {}
    user_input = data.get('message', '')
    sanitized_input = sanitize_input(user_input)
    return jsonify({"response": f"Processed: {sanitized_input}"}), 200

if __name__ == '__main__':
   import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)

