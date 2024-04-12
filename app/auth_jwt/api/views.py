from typing import Any

from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from app.auth_jwt.api.serializers import (
    TokenInputSerializer,
    TokenOutputSerializer,
)
from app.core.api.generics import CreateApiView
from app.core.services import get_tokens_for_user, get_user_by_id


class TokenCreateView(CreateApiView):
    """
    Get user token by id.
    In the production environment, needs to be changed the authorization by user data
    """

    permission_classes = (AllowAny,)
    serializer_class = TokenInputSerializer

    @extend_schema(responses={201: TokenOutputSerializer()})
    def post(self, request: Request, **kwargs: dict[str, Any]) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_user_by_id(serializer.validated_data.get('id'))
        refresh_token, access_token = get_tokens_for_user(user)

        output_serializer = TokenOutputSerializer(
            data={
                'refresh_token': refresh_token,
                'access_token': access_token
            }
        )
        output_serializer.is_valid(raise_exception=False)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)
