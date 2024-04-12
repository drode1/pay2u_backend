from django.urls import path

from app.auth_jwt.api.views import TokenCreateView

app_name = 'auth_jwt'

token_urlpatterns = [
    path('get-token/', TokenCreateView.as_view(), name='get_jwt_token'),
]
