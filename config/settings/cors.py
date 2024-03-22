import os

from app.core.utils import real_bool

CORS_ALLOW_ALL_ORIGINS: bool = real_bool(os.environ.get('CORS_ALLOW_ALL_ORIGINS', False))

if not CORS_ALLOW_ALL_ORIGINS:
    CORS_ALLOWED_ORIGINS: list = os.environ.get('CORS_ALLOWED_ORIGINS','').split(',')
    CORS_URLS_REGEX: str = str(os.environ.get('CORS_URLS_REGEX', ''))
