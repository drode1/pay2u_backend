from factory import django, Faker

from app.subscriptions.models import Category, Cashback, Invoice


class CategoryFactory(django.DjangoModelFactory):

    class Meta:
        model = Category

    name = Faker(
        'random_element',
        elements=('Музыка', 'Фильмы', 'Игры', 'Книги')
    )


class CashbackFactory(django.DjangoModelFactory):

    class Meta:
        model = Cashback

    amount = Faker('random_number', digits=2, fix_len=True)


class InvoiceFactory(django.DjangoModelFactory):

    class Meta:
        model = Invoice

    amount = Faker('random_number', digits=3, fix_len=True)
