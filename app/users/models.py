import datetime
from typing import Any

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import QuerySet, Sum
from phonenumber_field.modelfields import PhoneNumberField

from app.core.utils import recover_object, soft_delete_object
from config.django.base import MAX_NAME_LENGTH


class CustomUserManager(BaseUserManager):
    def _create_user(
            self,
            email: str | None = None,
            password: str | None = None,
            **extra_fields: Any
    ) -> 'User':
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(
            self,
            email: str | None = None,
            password: str | None = None,
            **extra_fields: Any
    ) -> 'User':
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(
            self,
            email: str | None = None,
            password: str | None = None,
            **extra_fields: Any
    ) -> 'User':
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """ User base model. """

    username = None

    email = models.EmailField(
        'email',
        unique=True,
        blank=False,
        null=False,
    )

    first_name = models.CharField(
        'First name',
        max_length=MAX_NAME_LENGTH,
        blank=False,
        null=False,
    )
    last_name = models.CharField(
        'Last name',
        max_length=MAX_NAME_LENGTH,
        blank=False,
        null=False,
    )
    patronymic = models.CharField(
        'Patronymic',
        max_length=MAX_NAME_LENGTH,
        blank=False,
        null=False,
    )
    phone = PhoneNumberField(
        'phone number',
        blank=False,
        null=False,
    )

    updated_at = models.DateTimeField(
        'updated at',
        auto_now=True,
    )

    deleted_at = models.DateTimeField(
        'deleted at',
        null=True,
        blank=True,
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (
        'first_name',
        'last_name',
        'patronymic',
        'phone',
    )

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        db_table = 'clients'
        ordering = (
            'id',
            'email',
        )

    def __repr__(self) -> str:
        return f'User {self.id}'

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def soft_delete(self) -> None:
        return soft_delete_object(self)

    def recover(self) -> None:
        return recover_object(self)

    @property
    def is_deleted(self) -> bool:
        return bool if self.deleted_at else False

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.patronymic} {self.last_name}'

    def get_active_subscriptions(self) -> QuerySet:
        from app.subscriptions.models import ClientSubscription

        return ClientSubscription.objects.filter(
            client=self,
            is_active=True
        )

    @property
    def get_active_subscriptions_count(self) -> int:
        return self.get_active_subscriptions().count()

    @property
    def get_month_cashback(self) -> int:
        cashback = self.client_cashback_history.filter(
            created_at__month=datetime.datetime.now(tz=datetime.UTC).month
        ).aggregate(cashback=Sum('amount')).get('cashback')
        return cashback or 0

    @property
    def get_user_bank_accounts(self) -> list[dict]:
        # It`s mock function, not for production
        mock_data = [
            {
                'name': 'Платежный счет',
                'balance': 150000,
                'number': '40817810399910005678'
            },
            {
                'name': 'Накопительный счет',
                'balance': 2500000,
                'number': '40817840599910002345'
            },
            {
                'name': 'Зарплатный счет',
                'balance': 350000,
                'number': '40817810099910004312'
            }
        ]
        return mock_data
