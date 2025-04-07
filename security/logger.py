import logging
logging.basicConfig(filename='chatbot_security.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

def log_request(request):
    logging.info("Request: %s %s from %s", request.method, request.path, request.remote_addr)
