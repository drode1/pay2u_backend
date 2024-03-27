from factory import Faker, Iterator, django, fuzzy

from app.subscriptions.models import (
    Cashback,
    Category,
    Invoice,
    Promocode,
    Subscription,
    Tariff,
)


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


class PromocodeFactory(django.DjangoModelFactory):
    class Meta:
        model = Promocode

    name = Iterator(
        (
            'BlackFriday',
            'МАРТ8',
            'ФЕВРАЛЬ23',
            '15',
            '10',
            '5',
            'Mail5',
        )
    )
    is_active = True
    amount = Faker('random_number', digits=2, fix_len=True)


class SubscriptionFactory(django.DjangoModelFactory):
    class Meta:
        model = Subscription

    name = Iterator(
        (
            'Иви',
            'MEGOGO',
            'Spotify',
            'Okko',
            'MyBook',
            'ЛитРес',
            'КРУТО-ТВ',
        )
    )
    description = Faker('sentence')
    cashback = fuzzy.FuzzyChoice(
        Cashback.objects.all(),
        getter=lambda c: c
    )
    category = fuzzy.FuzzyChoice(
        Category.objects.all(),
        getter=lambda c: c
    )
    is_recommended = Faker('pybool', truth_probability=70)
    image = Faker('image_url', width=88, height=88)


class TariffFactory(django.DjangoModelFactory):
    class Meta:
        model = Tariff

    name = fuzzy.FuzzyChoice(
        (
            '1 месяц',
            '3 месяца',
            '6 месяцев',
            '12 месяцев',
        ),
        getter=lambda c: c
    )
    subscription = fuzzy.FuzzyChoice(
        Subscription.objects.all(),
        getter=lambda c: c
    )
    promocode = fuzzy.FuzzyChoice(
        Promocode.objects.all(),
        getter=lambda c: c
    )
    amount = fuzzy.FuzzyChoice(
        (
            99,
            169,
            199,
            279,
        ),
        getter=lambda c: c
    )
    description = Faker('sentence')
