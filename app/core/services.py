from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken, Token

from app.users.models import User


def get_user_by_id(user_id: int) -> User:
    return get_object_or_404(User, id=user_id)


def get_tokens_for_user(user: User) -> tuple[str, str]:
    refresh = RefreshToken.for_user(user)
    return str(refresh), str(refresh.access_token)
