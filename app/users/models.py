from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from app.core.utils import recover_object, soft_delete_object
from config.django.base import MAX_NAME_LENGTH


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
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

    def __repr__(self):
        return f'User {self.id}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def soft_delete(self):
        return soft_delete_object(self)

    def recover(self):
        return recover_object(self)

    @property
    def is_deleted(self):
        return True if self.deleted_at else False

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
