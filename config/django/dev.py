import factory

from .base import *  # noqa

SECRET_KEY: str = 'test-key'

DEBUG: bool = True

factory.Faker._DEFAULT_LOCALE = 'ru_RU'
