from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models

from app.core.utils import soft_delete_object, recover_object


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
        # TODO Дописать нужными полями
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'users'
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
