from django.contrib.auth.hashers import make_password
from factory import Faker, django

from app.users.models import User


class UserAdminFactory(django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = 'admin'
    last_name = 'admin'
    patronymic = 'admin'
    phone = '+79260000000'
    email = 'admin@test.ru'
    password = make_password('admin')
    is_staff = True
    is_superuser = True


class UserFactory(django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = Faker('first_name')
    last_name = Faker('last_name')
    patronymic = Faker('language_name')
    phone = '+79030000000'
    email = Faker('email')
    password = make_password('test')
