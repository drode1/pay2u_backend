from django.contrib.auth.hashers import make_password
from factory import django

from app.users.models import User


class UserAdminFactory(django.DjangoModelFactory):
    class Meta:
        model = User

    username = 'admin'
    email = 'admin@test.ru'
    password = make_password('admin')
    is_staff = True
    is_superuser = True
