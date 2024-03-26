from django.contrib.auth.hashers import make_password
from factory import django
from faker import Faker

from app.users.models import User

fake = Faker('ru_RU')

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

    first_name = fake.first_name()
    last_name = 'test'
    patronymic = 'test'
    phone = '+79991112234'
    email = 'test@test.ru'
    password = make_password('test')
    is_staff = False
    is_superuser = False
