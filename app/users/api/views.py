from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import get_object_or_404

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
from app.subscriptions.models import (
    ClientCashbackHistory,
    ClientSubscription,
    Subscription,
)
from app.users.api.filters import IsDeletedFilter
from app.users.api.serializers import (
    UserCashbackHistoryInputSerializer,
    UserCashbackHistoryOutputSerializer,
    UserReadOutputSerializer,
)
from app.users.models import User


class DetailUserApi(RetrieveApiView):
    serializer_class = UserReadOutputSerializer

    def get_object(self):
        return User.objects.filter(pk=self.request.user.pk).get()


class ListUserSubscriptionsApi(ListApiView):
    serializer_class = UserSubscriptionOutputSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('is_active',)
    filterset_class = IsDeletedFilter

    def get_queryset(self):
        return ClientSubscription.objects.filter(
            client=self.request.user
        ).order_by('expiration_date')


class ListUserCashbackHistoryApi(ListApiView):
    serializer_class = UserCashbackHistoryOutputSerializer

    def get_queryset(self):
        return ClientCashbackHistory.objects.filter(
            client=self.request.user
        ).order_by('-created_at')


class CashbackHistoryUpdateStatusApiView(UpdateApiView):
    serializer_class = UserCashbackHistoryInputSerializer
    response_serializer_class = UserCashbackHistoryOutputSerializer

    def get_object(self):
        filters = {
            'id': self.kwargs.get('cashback_id'),
            'client': self.request.user
        }
        return get_object_or_404(ClientCashbackHistory, **filters)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class SubscriptionCreateApiView(CreateApiView):
    queryset = Subscription.objects.without_trashed()
    serializer_class = UserSubscriptionCreteInputSerializer


class SubscriptionUpdateApiView(UpdateApiView):
    serializer_class = UserSubscriptionUpdateInputSerializer

    def get_object(self):
        filters = {
            'id': self.kwargs.get('subscription_id'),
            'client': self.request.user
        }
        return get_object_or_404(ClientSubscription, **filters)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class SubscriptionCancelApiView(SoftDestroyApiView):
    serializer_class = UserSubscriptionOutputSerializer

    def get_object(self):
        filters = {
            'id': self.kwargs.get('subscription_id'),
            'client': self.request.user
        }
        instance = get_object_or_404(ClientSubscription, **filters)
        return instance
