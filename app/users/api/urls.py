from django.urls import path

from app.users.api.views import (
    CashbackHistoryUpdateStatusApiView,
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
        'me/',
        DetailUserApi.as_view(),
        name='detail'
    ),
    path(
        'subscriptions/',
        ListUserSubscriptionsApi.as_view(),
        name='subscription_list'
    ),
    path(
        'cashback-history/',
        ListUserCashbackHistoryApi.as_view(),
        name='cashback_history_list'
    ),
    path(
        'cashback-history/<int:cashback_id>/change-status/',
        CashbackHistoryUpdateStatusApiView.as_view(),
        name='cashback_history_update'
    ),
    path(
        'subscriptions/create/',
        SubscriptionCreateApiView.as_view(),
        name='subscription_create'
    ),
    path(
        'subscriptions/<int:subscription_id>/update/',
        SubscriptionUpdateApiView.as_view(),
        name='subscription_update'
    ),
    path(
        'subscriptions/<int:subscription_id>/delete/',
        SubscriptionCancelApiView.as_view(),
        name='subscription_delete'
    ),
]
