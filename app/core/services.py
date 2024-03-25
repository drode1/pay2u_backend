from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from app.users.models import User


def get_user_by_id(request):
    try:
        user = User.objects.get(id=request.data.get('id'))

    except User.DoesNotExist:
        return Response(
            {'user': 'Not Found'},
            status=status.HTTP_404_NOT_FOUND
        )
    return user


def get_token(user):
    token = RefreshToken.for_user(user)
    return Response({'refresh': str(token),
                     'access': str(token.access_token)},
                    status=status.HTTP_201_CREATED)
