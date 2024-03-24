from django.urls import path

from app.users.api.views import DetailUserApi

# TODO Оставляю паттерны, чтобы мог посмотреть как они устроены

user_patterns = [
    path('<int:pk>/', DetailUserApi.as_view(), name='detail'),
]

#     path('', ListUserApi.as_view(), name='list'),
#     path('<int:pk>/', DetailUserApi.as_view(), name='detail'),
#     path('me/', DetailUserMeAPI.as_view(), name='self'),
#     path('create/', CreateUserApi.as_view(), name='create'),
#     path('<int:pk>/update/', UpdateUserApi.as_view(), name='update'),
#     path('<int:pk>/delete/', DeleteUserApi.as_view(), name='delete'),
#     path('<int:pk>/recover/', RecoverUserApi.as_view(), name='recover'),