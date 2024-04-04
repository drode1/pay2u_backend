from django.urls import path

from app.users.api.views import (
    DetailUserApi,
    ListUserCashbackHistoryApi,
    ListUserSubscriptionsApi,
    SubscriptionCancelApiView,
    SubscriptionCreateApiView,
    SubscriptionUpdateApiView,
)

app_name = 'clients'

user_patterns = [
    path(
        '<int:pk>/',
        DetailUserApi.as_view(),
        name='detail'
    ),
    path(
        '<int:pk>/subscriptions/',
        ListUserSubscriptionsApi.as_view(),
        name='subscription_list'
    ),
    path(
        '<int:pk>/cashback-history/',
        ListUserCashbackHistoryApi.as_view(),
        name='subscription_list'
    ),
    path(
        'subscriptions/create/',
        SubscriptionCreateApiView.as_view(),
        name='subscription_create'
    ),
    path(
        '<int:pk>/subscriptions/<int:subscription_id>/update/',
        SubscriptionUpdateApiView.as_view(),
        name='subscription_update'
    ),
    path(
        '<int:pk>/subscriptions/<int:subscription_id>/delete/',
        SubscriptionCancelApiView.as_view(),
        name='subscription_delete'
    ),
]
