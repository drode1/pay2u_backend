from django.contrib.auth.hashers import make_password
from factory import django, Faker

from app.users.models import User


class UserAdminFactory(django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = 'admin'
    last_name = 'adminov'
    patronymic = 'adminovich'
    phone = '+79991112233'
    email = 'admin@test.ru'
    password = make_password('admin')
    is_staff = True
    is_superuser = True


class UserFactory(django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = Faker('first_name_male')
    last_name = Faker('last_name_male')
    patronymic = Faker('middle_name_male')
    phone = Faker('phone_number')
    email = Faker('email')
    password = make_password('test')
    is_staff = False
    is_superuser = False
