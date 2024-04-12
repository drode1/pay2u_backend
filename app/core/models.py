from django.db import models
from django.db.models import QuerySet

from app.core.utils import recover_object, soft_delete_object


class BaseModelQuerySet(QuerySet):
    def without_trashed(self):
        return self.filter(deleted_at__isnull=True)

    def only_trashed(self):
        return self.filter(deleted_at__isnull=False)


class BaseModelManager(models.Manager):
    def get_queryset(self):
        return BaseModelQuerySet(self.model)

    def without_trashed(self):
        return self.get_queryset().without_trashed()

    def only_trashed(self):
        return self.get_queryset().only_trashed()


class BaseModel(models.Model):
    """ Base model. """

    created_at = models.DateTimeField('created at', auto_now_add=True)

    updated_at = models.DateTimeField('updated at', auto_now=True)

    deleted_at = models.DateTimeField('deleted at', null=True, blank=True)

    objects = BaseModelManager()

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return str(self.id)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} {self.id}'

    @property
    def is_deleted(self) -> bool:
        return bool(self.deleted_at)

    def soft_delete(self) -> None:
        return soft_delete_object(self)

    def recover(self) -> None:
        return recover_object(self)
