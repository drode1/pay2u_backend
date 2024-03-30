from django.urls import path

from app.users.api.views import DetailUserApi

app_name = 'clients'

user_patterns = [
    path('<int:pk>/', DetailUserApi.as_view(), name='detail'),
]
