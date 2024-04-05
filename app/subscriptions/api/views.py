from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from app.core.api.generics import (
    CreateApiView,
    DestroyApiView,
    ListApiView,
    RetrieveApiView,
)
from app.subscriptions.api.serializers import (
    CategoryReadOutputSerializer,
    FavouriteInputSerializer,
    FavouriteOutputSerializer,
    SubscriptionReadOutputSerializer,
)
from app.subscriptions.models import Category, Favourite, Subscription


class CategoryListApiView(ListApiView):
    """List of subscription categories"""
    queryset = Category.objects.without_trashed()
    serializer_class = CategoryReadOutputSerializer


class SubscriptionListApiView(ListApiView):
    """List of available subscriptions"""
    queryset = Subscription.objects.without_trashed()
    serializer_class = SubscriptionReadOutputSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    )
    filterset_fields = ('is_recommended',)
    ordering_fields = (
        'cashback__amount',
        'subscription_tariff__amount',
        'popularity',
    )
    search_fields = (
        'name',
        'description',
        'category__name',
    )


class DetailSubscriptionApiView(RetrieveApiView):
    """Detail view of one subscription"""
    queryset = Subscription.objects.without_trashed()
    serializer_class = SubscriptionReadOutputSerializer


class FavouriteListApiView(ListApiView):
    """List of user`s favourite subscriptions"""
    serializer_class = FavouriteOutputSerializer

    def get_queryset(self):
        user = self.request.user
        return Favourite.objects.filter(client=user)


class FavouriteCreateApiView(CreateApiView):
    """Mark subscription as favourite"""
    serializer_class = FavouriteInputSerializer
    response_serializer_class = FavouriteOutputSerializer

    def get_queryset(self):
        user = self.request.user
        return Favourite.objects.filter(client=user)


class FavouriteDestroyApiView(DestroyApiView):
    """Unmark subscription as favourite"""
    serializer_class = FavouriteInputSerializer

    def get_object(self):
        serializer = self.get_serializer(
            data=self.request.data
        )
        serializer.is_valid(raise_exception=False)
        instance = Favourite.objects.filter(
            subscription_id=serializer.data['subscription'],
            client=self.request.user
        )
        return instance
