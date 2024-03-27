from django.urls import path

from app.subscriptions.api.views import CategoryListApiView

app_name = 'subscriptions'

subscriptions_urlpatterns = [
    path(
        'categories/list/',
        CategoryListApiView.as_view(),
        name='category_list'
    ),
]

