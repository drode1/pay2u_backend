from django_filters.rest_framework import DjangoFilterBackend

from app.core.api.generics import (
    CreateApiView,
    ListApiView,
    RetrieveApiView,
    SoftDestroyApiView,
    UpdateApiView,
)
from app.subscriptions.api.serializers import (
    UserSubscriptionCreteInputSerializer,
    UserSubscriptionOutputSerializer,
    UserSubscriptionUpdateInputSerializer,
)
from app.subscriptions.models import ClientSubscription, Subscription
from app.users.api.filters import IsDeletedFilter
from app.users.api.permissions import IsOwner
from app.users.api.serializers import UserReadOutputSerializer
from app.users.models import User


class DetailUserApi(RetrieveApiView):
    queryset = User.objects.all()
    serializer_class = UserReadOutputSerializer
    permission_classes = (IsOwner,)
    lookup_field = 'pk'


class ListUserSubscriptionsApi(ListApiView):
    serializer_class = UserSubscriptionOutputSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('is_active',)
    filterset_class = IsDeletedFilter

    def get_queryset(self):
        return ClientSubscription.objects.filter(client=self.request.user)


class SubscriptionCreateApiView(CreateApiView):
    queryset = Subscription.objects.without_trashed()
    serializer_class = UserSubscriptionCreteInputSerializer


class SubscriptionUpdateApiView(UpdateApiView):
    serializer_class = UserSubscriptionUpdateInputSerializer

    def get_queryset(self):
        return ClientSubscription.objects.filter(
            id=self.kwargs.get('subscription_id'),
            client=self.request.user
        )

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class SubscriptionCancelApiView(SoftDestroyApiView):
    serializer_class = UserSubscriptionOutputSerializer

    def get_object(self):
        instance = ClientSubscription.objects.filter(
            id=self.kwargs.get('subscription_id'),
            client=self.request.user
        ).get()
        return instance
