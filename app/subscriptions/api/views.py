from django_filters.rest_framework import DjangoFilterBackend

from app.core.api.generics import ListApiView, RetrieveApiView
from app.subscriptions.api.serializers import (
    CategoryReadOutputSerializer,
    SubscriptionReadOutputSerializer,
)
from app.subscriptions.models import Category, Subscription


class CategoryListApiView(ListApiView):
    queryset = Category.objects.without_trashed()
    serializer_class = CategoryReadOutputSerializer


class SubscriptionListApiView(ListApiView):
    queryset = Subscription.objects.without_trashed()
    serializer_class = SubscriptionReadOutputSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('is_recommended',)


class DetailSubscriptionApiView(RetrieveApiView):
    queryset = Subscription.objects.without_trashed()
    serializer_class = SubscriptionReadOutputSerializer
