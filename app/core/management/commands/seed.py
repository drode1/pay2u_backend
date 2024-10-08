import logging

from django.core.management.base import BaseCommand
from django.db.models import Model

from app.subscriptions.factories import (
    CashbackFactory,
    CategoryFactory,
    ClientSubscriptionFactory,
    SubscriptionBenefitsFactory,
    SubscriptionFactory,
    TariffFactory,
)
from app.subscriptions.models import (
    Cashback,
    Category,
    ClientSubscription,
    Invoice,
    Promocode,
    Subscription,
    SubscriptionBenefits,
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
        SubscriptionFactory: 7,
        TariffFactory: 21,
        ClientSubscriptionFactory: 2,
        SubscriptionBenefitsFactory: 10
    }

    MODELS = (
        User,
        Cashback,
        Tariff,
        Subscription,
        Category,
        ClientSubscription,
        Promocode,
        Invoice,
        SubscriptionBenefits,
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
        except Exception:
            logger.exception('An error occurred during data generation')
            raise Exception # noqa: TRY002
        else:
            logger.info('Test data generation was successful.')
