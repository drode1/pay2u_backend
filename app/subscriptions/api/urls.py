from django.urls import path

from app.subscriptions.api.views import (
    CategoryListApiView,
    DetailSubscriptionApiView,
    FavouriteCreateApiView,
    FavouriteDestroyApiView,
    FavouriteListApiView,
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
        FavouriteListApiView.as_view(),
        name='favourite_subscription'
    ),
    path(
        'favourites/add/',
        FavouriteCreateApiView.as_view(),
        name='add_favourite_subscription'
    ),
    path(
        'favourites/delete/',
        FavouriteDestroyApiView.as_view(),
        name='delete_favourite_subscription'
    ),
]
