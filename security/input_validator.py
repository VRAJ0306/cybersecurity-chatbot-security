import re
def sanitize_input(user_input: str) -> str:
    sanitized = re.sub(r'<.*?>', '', user_input)
    sanitized = re.sub(r'[^\w\s,.?!]', '', sanitized)
    return sanitized.strip()
