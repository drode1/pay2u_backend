import os

CORS_ALLOW_ALL_ORIGINS: bool = bool(os.environ.get('CORS_ALLOW_ALL_ORIGINS', True))

if not CORS_ALLOW_ALL_ORIGINS:
    CORS_ALLOWED_ORIGINS: list = os.environ.get('CORS_ALLOWED_ORIGINS','').split(',')
    CORS_URLS_REGEX: str = str(os.environ.get('CORS_URLS_REGEX', ''))
