from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken

from app.users.models import User


def get_user_by_id(user_id: int):
    return get_object_or_404(User, id=user_id)


def get_tokens(user: User):
    token = RefreshToken.for_user(user)
    return token, token.access_token
