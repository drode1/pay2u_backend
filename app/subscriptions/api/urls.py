from django.urls import path

from app.subscriptions.api.views import (
    CategoryListApiView,
    DetailSubscriptionApiView,
    LikeSubscriptionApiView,
    SubscriptionListApiView,
    UnLikeSubscriptionApiView,
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
        '<int:pk>/like/',
        LikeSubscriptionApiView.as_view(),
        name='subscription_like'
    ),
    path(
        '<int:pk>/unlike/',
        UnLikeSubscriptionApiView.as_view(),
        name='subscription_unlike'
    ),
]
