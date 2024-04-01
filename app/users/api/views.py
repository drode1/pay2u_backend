from django_filters.rest_framework import DjangoFilterBackend

from app.core.api.generics import ListApiView, RetrieveApiView
from app.subscriptions.api.serializers import UserSubscriptionOutputSerializer
from app.subscriptions.models import ClientSubscription
from app.users.api.permissions import IsOwner
from app.users.api.serializers import UserReadOutputSerializer
from app.users.models import User


class DetailUserApi(RetrieveApiView):
    """View for retrieving one user."""

    queryset = User.objects.all()
    serializer_class = UserReadOutputSerializer
    permission_classes = (IsOwner,)
    lookup_field = 'pk'


class ListUserSubscriptionsApi(ListApiView):
    permission_classes = (IsOwner,)
    serializer_class = UserSubscriptionOutputSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('is_active',)

    def get_queryset(self):
        return ClientSubscription.objects.filter(client=self.request.user)
