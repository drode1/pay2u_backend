from django_filters.rest_framework import DjangoFilterBackend

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


class FavouriteListApiView(ListApiView):
    serializer_class = FavouriteOutputSerializer

    def get_queryset(self):
        user = self.request.user
        return Favourite.objects.filter(client=user)


class FavouriteCreateApiView(CreateApiView):
    serializer_class = FavouriteInputSerializer
    response_serializer_class = FavouriteOutputSerializer

    def get_queryset(self):
        user = self.request.user
        return Favourite.objects.filter(client=user)


class FavouriteDestroyApiView(DestroyApiView):
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
