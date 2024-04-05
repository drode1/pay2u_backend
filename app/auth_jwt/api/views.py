from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from app.auth_jwt.api.serializers import TokenInputSerializer
from app.core.api.generics import CreateApiView
from app.core.services import get_tokens_for_user, get_user_by_id


class TokenCreateView(CreateApiView):
    """
    Get user token by id.
    In the production environment, needs to be changed the authorization by user data
    """
    permission_classes = (AllowAny,)
    serializer_class = TokenInputSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_user_by_id(request.data.get('id'))
        refresh_token, access_token = get_tokens_for_user(user)

        return Response(
            {
                'refresh_token': str(refresh_token),
                'access_token': str(access_token)
            },
            status=status.HTTP_201_CREATED
        )
