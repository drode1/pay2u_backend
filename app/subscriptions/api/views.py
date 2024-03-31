from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response

from app.core.api.generics import CreateApiView, ListApiView, RetrieveApiView
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
    filterset_fields = ('is_recommended', 'is_liked',)


class DetailSubscriptionApiView(RetrieveApiView):
    queryset = Subscription.objects.without_trashed()
    serializer_class = SubscriptionReadOutputSerializer


class LikeSubscriptionApiView(CreateApiView):
    queryset = Subscription.objects.without_trashed()
    response_serializer_class = SubscriptionReadOutputSerializer

    def create(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_liked = True
        instance.save()
        serialized_data = self.response_serializer_class(instance).data

        return Response(serialized_data, status=status.HTTP_200_OK)


class UnLikeSubscriptionApiView(CreateApiView):
    queryset = Subscription.objects.without_trashed()
    response_serializer_class = SubscriptionReadOutputSerializer

    def create(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_liked = False
        instance.save()
        serialized_data = self.response_serializer_class(instance).data

        return Response(serialized_data, status=status.HTTP_200_OK)
