from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from app.auth_jwt.api.serializers import TokenOutputSerializer
from app.core.services import get_user_by_id, get_tokens


class TokenCreateView(CreateAPIView):
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = TokenOutputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_user_by_id(request.data.get('id'))
        refresh_token, access_token = get_tokens(user)
        return Response(
            {
                'refresh': str(refresh_token),
                'access': str(refresh_token)
            },
            status=status.HTTP_201_CREATED
        )
