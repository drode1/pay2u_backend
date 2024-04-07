from datetime import datetime as dt
from datetime import timedelta

from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models import QuerySet

from app.subscriptions import enums
from app.subscriptions.api.exceptions import (
    PaymentException,
    WrongCashbackStatusException,
)
from app.subscriptions.models import (
    ClientCashbackHistory,
    ClientSubscription,
    Invoice,
    Promocode,
    Subscription,
    Tariff,
)
from app.users.models import User


def create_invoice_with_tariff_amount(tariff_amount: int) -> Invoice:
    invoice = Invoice.objects.create(
        amount=tariff_amount
    )
    return invoice


def validate_tariff_subscription(
        tariff_id: Tariff.pk,
        subscription_id: Subscription.pk,
        is_deleted: bool = True
) -> QuerySet[Tariff]:
    from app.subscriptions.models import Tariff

    kwargs = {
        'id': tariff_id,
        'subscription_id': subscription_id,
        'deleted_at__isnull': is_deleted
    }

    tariffs = Tariff.objects.filter(**kwargs)

    if not tariffs.exists():
        raise ValidationError(
            'Selected tariff does not match the subscription'
        )
    return tariffs


def calculate_expiration_date(tariff_days_amount) -> dt:
    return dt.now() + timedelta(days=tariff_days_amount)


def renew_client_subscription(client_subscription) -> ClientSubscription:
    promocode = Promocode.objects.create()  # Create new promocode
    new_subscription = client_subscription.__class__.objects.create(
        client=client_subscription.client,
        subscription=client_subscription.subscription,
        tariff=client_subscription.tariff,
        promocode=promocode,
        expiration_date=calculate_expiration_date(
            client_subscription.tariff.days_amount
        ),
        # Calculate how many days subscription should be
        invoice=create_invoice_with_tariff_amount(
            client_subscription.tariff.amount
        ),
        # Create new invoice
        is_active=client_subscription.is_active,
        is_auto_pay=client_subscription.is_auto_pay
    )
    promocode.activate()
    return new_subscription


def inactivate_or_renew_user_subscription(
        client_subscription: ClientSubscription
) -> ClientSubscription:
    now = dt.now().date()

    if not client_subscription.is_active:
        return client_subscription

    if client_subscription.is_deleted:
        return client_subscription

    if client_subscription.is_auto_pay and client_subscription.expiration_date < now:
        return renew_client_subscription(client_subscription)

    if client_subscription.expiration_date < now:
        client_subscription.is_active = False
        client_subscription.soft_delete()

    return client_subscription


def is_current_user_subscription_exists(client, subscription):
    return ClientSubscription.objects.filter(
        client=client,
        subscription=subscription,
        is_active=True,
        expiration_date__gte=dt.now().date()
    ).exists()


def create_new_user_subscription(data: dict):
    tariff: Tariff = data.get('tariff')
    account = data.get('charge_account')
    subscription: Subscription = data.get('subscription')
    client: User = data.get('client')

    payment_amount = tariff.amount * (tariff.days_amount // 30)

    process_payment(account, payment_amount)
    new_subscription = create_subscription(
        subscription,
        tariff,
        client,
        payment_amount,
        data.get('is_auto_pay'),
    )

    set_client_cashback(client, new_subscription, subscription.cashback.amount,
                        payment_amount)

    return new_subscription


@transaction.atomic
def create_subscription(
        subscription,
        tariff,
        client,
        payment_amount,
        is_auto_pay=False,
):
    promocode = Promocode.objects.create()  # Create new promocode
    new_invoice = create_invoice_with_tariff_amount(payment_amount)
    new_subscription = ClientSubscription.objects.create(
        client=client,
        subscription=subscription,
        tariff=tariff,
        promocode=promocode,
        expiration_date=calculate_expiration_date(tariff.days_amount),
        invoice=new_invoice,
        is_active=True,
        is_auto_pay=is_auto_pay
    )
    return new_subscription


def process_payment(account: int, amount: int):
    try:
        # Fake processing payment function
        charge_money(account, amount)
    except PaymentException as err:
        raise PaymentException from err
    except Exception as e:
        raise e
    return True


def charge_money(account: int, amount: int):
    ...


def calculate_cashback_amount(amount: int, percent: int):
    return (amount * percent) // 100


def set_client_cashback(
        client: User,
        subscription: ClientSubscription,
        cashback_percent: int,
        amount: int
) -> None:
    cashback_amount = calculate_cashback_amount(amount, cashback_percent)

    ClientCashbackHistory.objects.create(
        client=client,
        amount=cashback_amount,
        status=enums.CashbackHistoryStatus.PENDING,
        client_subscription=subscription
    )

    return None


def update_cashback_history_status(
        instance: ClientCashbackHistory,
        status: enums.CashbackHistoryStatus.choices
):
    if instance.status != enums.CashbackHistoryStatus.PENDING.value:
        raise WrongCashbackStatusException
    instance.status = status
    instance.save()
