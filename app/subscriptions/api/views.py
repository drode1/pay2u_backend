from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response

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


class FavouriteListCreateDestroyApiView(
    ListApiView,
    CreateApiView,
    DestroyApiView
):
    serializer_class = FavouriteOutputSerializer
    response_serializer_class = FavouriteOutputSerializer

    def get_queryset(self):
        user = self.request.user
        return Favourite.objects.filter(client=user)

    def get_serializer_class(self):
        if self.request.method in ('POST', 'DELETE'):
            return FavouriteInputSerializer
        return self.serializer_class

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=False)
        instance = Favourite.objects.filter(
            subscription_id=serializer.data['subscription'],
            client=request.user
        )
        self.perform_destroy(instance=instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
