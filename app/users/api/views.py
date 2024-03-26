from rest_framework import status
from rest_framework.response import Response

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


class DetailUserMeAPI(RetrieveApiView):
    """View for retrieving my self."""

    serializer_class = UserReadOutputSerializer

    # permission_classes = [IsOwner]

    def retrieve(self, request, *args, **kwargs):
        instance = request.user
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
