from django.urls import path

from app.subscriptions.api.views import SubscriptionCreateApiView
from app.users.api.views import DetailUserApi, ListUserSubscriptionsApi

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
        'subscriptions/create/',
        SubscriptionCreateApiView.as_view(),
        name='subscription_create'
    ),
]
