from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

from app.auth_jwt.api.serializers import TokenSerializer

from app.users.models import User


class TokenCreateView(CreateAPIView):
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = User.objects.get(id=request.data.get('id'))
        except User.DoesNotExist:
            return Response(
                {'username': 'Not Found'},
                status=status.HTTP_404_NOT_FOUND
            )
        print(request.data.get('id'))
        print(request.user)

        token = RefreshToken.for_user(user)
        return Response({'refresh': str(token),
                         'access': str(token.access_token)},
                        status=status.HTTP_201_CREATED)
