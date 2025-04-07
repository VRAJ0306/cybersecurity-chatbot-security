from functools import wraps
from flask import request, jsonify
VALID_API_KEYS = {"your-secure-api-key"}

def require_api_key(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        api_key = request.headers.get('x-api-key')
        if api_key not in VALID_API_KEYS:
            return jsonify({"error": "Unauthorized"}), 401
        return func(*args, **kwargs)
    return wrapper
