from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView

from app.auth_jwt.api.serializers import TokenOutputSerializer
from app.core.services import get_user_by_id, get_token


class TokenCreateView(CreateAPIView):
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = TokenOutputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_user_by_id(request)
        return get_token(user)
