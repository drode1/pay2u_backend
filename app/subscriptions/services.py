import secrets
import string
from datetime import datetime as dt
from datetime import timedelta

from django.core.exceptions import ValidationError

from app.subscriptions.models import Invoice, Promocode


def create_new_code_for_promocode():
    code_length = 6
    while True:
        code = ''.join(
            secrets.choice(string.ascii_uppercase + string.digits) for _ in
            range(code_length)
        )
        if not Promocode.objects.filter(name=code).exists():
            return code


def create_invoice_with_tariff_amount(tariff):
    invoice = Invoice.objects.create(
        amount=tariff.amount
    )
    return invoice


def validate_tariff_subscription(tariff_id: int, subscription_id: int):
    from app.subscriptions.models import Tariff

    tariffs = Tariff.objects.filter(
        id=tariff_id,
        subscription_id=subscription_id
    )

    if not tariffs.exists():
        raise ValidationError(
            'Selected tariff does not match the subscription'
        )
    return tariffs


def calculate_tariff_expiration_date(
        subscription_created_at,
        subscription_expiration_date
):
    if isinstance(subscription_created_at, dt):
        subscription_created_at = subscription_created_at.date()

    delta = subscription_expiration_date - subscription_created_at
    return dt.now() + timedelta(days=delta.days)


def renew_client_subscription(client_subscription):
    new_subscription = client_subscription.__class__.objects.create(
        client=client_subscription.client,
        subscription=client_subscription.subscription,
        tariff=client_subscription.tariff,
        promocode=Promocode.objects.create(),  # Create new promocode
        expiration_date=calculate_tariff_expiration_date(
            client_subscription.created_at,
            client_subscription.expiration_date
        ),
        # Calculate how many days subscription should be
        invoice=create_invoice_with_tariff_amount(client_subscription.tariff),
        # Create new invoice
        is_active=client_subscription.is_active,
        is_liked=client_subscription.is_liked,
        is_auto_pay=client_subscription.is_auto_pay
    )
    return new_subscription


def inactivate_or_renew_user_subscription(client_subscription):
    now = dt.now().date()
    if not client_subscription.is_active:
        return client_subscription

    if client_subscription.is_auto_pay and client_subscription.expiration_date < (
            now + timedelta(days=1)):
        return renew_client_subscription(client_subscription)

    if client_subscription.expiration_date < now:
        client_subscription.is_active = False
        client_subscription.soft_delete()

    return client_subscription
