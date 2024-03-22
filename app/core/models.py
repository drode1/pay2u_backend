from django.db import models

from app.core.utils import (
    soft_delete_object,
    recover_object
)


class BaseModel(models.Model):
    """ Base model. """

    created_at = models.DateTimeField('created at', auto_now_add=True)

    updated_at = models.DateTimeField('updated at', auto_now=True)

    deleted_at = models.DateTimeField('deleted at', null=True, blank=True)

    class Meta:
        abstract = True

    @property
    def is_deleted(self):
        return True if self.deleted_at else False

    def soft_delete(self):
        return soft_delete_object(self)

    def recover(self):
        return recover_object(self)
