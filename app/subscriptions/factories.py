from factory import Faker, Iterator, SubFactory, django, fuzzy, lazy_attribute

from app.subscriptions.enums import SubscriptionPeriod
from app.subscriptions.models import (
    Cashback,
    Category,
    ClientSubscription,
    Invoice,
    Promocode,
    Subscription,
    Tariff,
)
from app.users.models import User


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

    is_active = True


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
    image_preview = Faker('image_url', width=88, height=88)
    image_detail = Faker('image_url', width=264, height=264)


class TariffFactory(django.DjangoModelFactory):
    class Meta:
        model = Tariff

    days_amount = fuzzy.FuzzyChoice(
        SubscriptionPeriod.choices,
        getter=lambda c: c[0]
    )
    subscription = fuzzy.FuzzyChoice(
        Subscription.objects.all(),
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


class ClientSubscriptionFactory(django.DjangoModelFactory):
    class Meta:
        model = ClientSubscription

    client = fuzzy.FuzzyChoice(
        User.objects.all(),
        getter=lambda c: c
    )
    subscription = fuzzy.FuzzyChoice(
        Subscription.objects.all(),
        getter=lambda c: c
    )
    promocode = SubFactory(PromocodeFactory)
    invoice = SubFactory(InvoiceFactory)
    is_liked = Faker('pybool', truth_probability=50)
    is_auto_pay = Faker('pybool', truth_probability=20)

    @lazy_attribute
    def tariff(self):
        # Get list of tariffs which linked to concrete subscription
        tariffs = Tariff.objects.filter(subscription=self.subscription)
        if tariffs.exists():
            return fuzzy.FuzzyChoice(tariffs).fuzz()
