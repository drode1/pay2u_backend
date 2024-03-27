from factory import Faker, Iterator, django

from app.subscriptions.models import Cashback, Category, Invoice


class CategoryFactory(django.DjangoModelFactory):
    class Meta:
        model = Category

    name = Iterator(
        (
            'Музыка',
            'Фильмы',
            'Игры',
            'Книги',
        )
    )


class CashbackFactory(django.DjangoModelFactory):
    class Meta:
        model = Cashback

    amount = Faker('random_number', digits=2, fix_len=True)


class InvoiceFactory(django.DjangoModelFactory):
    class Meta:
        model = Invoice

    amount = Faker('random_number', digits=3, fix_len=True)
