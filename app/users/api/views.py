from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
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
from app.users.api.filters import ClientSubscriptionFilter
from app.users.api.serializers import (
    UserCashbackHistoryInputSerializer,
    UserCashbackHistoryOutputSerializer,
    UserReadOutputSerializer,
)
from app.users.models import User


class DetailUserApi(RetrieveApiView):
    """Detail user"""
    serializer_class = UserReadOutputSerializer

    def get_object(self):
        return User.objects.filter(pk=self.request.user.pk).get()


class ListUserSubscriptionsApi(ListApiView):
    """List of user`s subscriptions"""
    serializer_class = UserSubscriptionOutputSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClientSubscriptionFilter

    def get_queryset(self):
        return ClientSubscription.objects.filter(
            client=self.request.user
        ).order_by('expiration_date')


class ListUserCashbackHistoryApi(ListApiView):
    """List of user`s cashback history"""
    serializer_class = UserCashbackHistoryOutputSerializer

    def get_queryset(self):
        return ClientCashbackHistory.objects.filter(
            client=self.request.user
        ).order_by('-created_at')


@extend_schema(methods=['PUT'], exclude=True)
class CashbackHistoryUpdateStatusApiView(UpdateApiView):
    """Update cashback status"""
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
    """Create new user subscription"""
    queryset = Subscription.objects.without_trashed()
    serializer_class = UserSubscriptionCreteInputSerializer


@extend_schema(methods=['PUT'], exclude=True)
class SubscriptionUpdateApiView(UpdateApiView):
    """Update subscription information"""
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
    """Update subscription information"""
    serializer_class = UserSubscriptionOutputSerializer

    def get_object(self):
        filters = {
            'id': self.kwargs.get('subscription_id'),
            'client': self.request.user
        }
        instance = get_object_or_404(ClientSubscription, **filters)
        instance.is_auto_pay = False
        return instance
