import logging

from django.core.management.base import BaseCommand
from django.db.models import Model

from app.subscriptions.factories import (
    CashbackFactory,
    CategoryFactory,
    InvoiceFactory,
    PromocodeFactory,
    SubscriptionFactory,
    TariffFactory,
)
from app.subscriptions.models import (
    Cashback,
    Category,
    Invoice,
    Promocode,
    Subscription,
    Tariff,
)
from app.users.factories import UserAdminFactory, UserFactory
from app.users.models import User

logger = logging.getLogger()


class Command(BaseCommand):
    help = 'Test data generation'  # noqa: A003

    FACTORIES = {
        UserAdminFactory: 1,
        UserFactory: 1,
        CategoryFactory: 4,
        CashbackFactory: 5,
        InvoiceFactory: 5,
        PromocodeFactory: 7,
        SubscriptionFactory: 7,
        TariffFactory: 21,
    }

    MODELS = (
        User,
        Cashback,
        Invoice,
        Promocode,
        Tariff,
        Subscription,
        Category,
    )

    def clean_db(self, models: [Model]) -> None:
        for model in models:
            model.objects.all().delete()

    def seed_data(self, factories: dict) -> None:
        for factory, amount in factories.items():
            for _ in range(amount):
                factory()

    def handle(self, *args, **options):
        try:
            self.clean_db(self.MODELS)
            self.seed_data(self.FACTORIES)
        except Exception as e:
            logger.error(f'An error occurred during data generation: {e}')
            raise e
        else:
            logger.info('Test data generation was successful.')
