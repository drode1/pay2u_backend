from app.core.api.generics import RetrieveApiView
from app.users.api.permissions import IsOwner
from app.users.api.serializers import UserReadOutputSerializer
from app.users.models import User


class DetailUserApi(RetrieveApiView):
    """View for retrieving one user."""

    queryset = User.objects.all()
    serializer_class = UserReadOutputSerializer
    permission_classes = (IsOwner,)
    lookup_field = 'pk'
