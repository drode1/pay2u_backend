from django.urls import path

from app.subscriptions.api.views import (
    CategoryListApiView,
    DetailSubscriptionApiView,
    FavouriteListCreateDestroyApiView,
    SubscriptionListApiView,
)

app_name = 'subscriptions'

subscriptions_urlpatterns = [
    path(
        'categories/',
        CategoryListApiView.as_view(),
        name='categories_list'
    ),
    path(
        'list/',
        SubscriptionListApiView.as_view(),
        name='subscriptions_list'
    ),
    path(
        '<int:pk>/',
        DetailSubscriptionApiView.as_view(),
        name='subscription_detail'
    ),
    path(
        'favourites/',
        FavouriteListCreateDestroyApiView.as_view(),
        name='favourite_subscription'
    ),
]
