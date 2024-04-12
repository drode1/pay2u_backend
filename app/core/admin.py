from typing import Any, Protocol, Sequence, Type

from django.contrib import admin, messages
from django.db import models
from django.http import HttpRequest
from django.utils.timezone import now
from django.utils.translation import ngettext
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class DjangoModelAdminProtocol(Protocol):

    @property
    def add_fieldsets(self) -> Sequence[tuple[str | None, Any]]: ...


@admin.action(description='Delete')
def make_object_deleted_at(modeladmin, request, queryset) -> None:
    updated = queryset.update(deleted_at=now())

    message = ngettext(
        '%(count)d %(model)s was deleted.',
        '%(count)d %(models)s were deleted.',
        updated
    ) % {'count': updated,
         'model': modeladmin.opts.verbose_name,
         'models': modeladmin.opts.verbose_name_plural,
         }

    modeladmin.message_user(
        request,
        message,
        messages.SUCCESS
    )


@admin.action(description='Recover')
def recover_object(modeladmin, request, queryset):
    updated = queryset.update(deleted_at=None)

    message = ngettext(
        '%(count)d %(model)s was recovered.',
        '%(count)d %(models)s were recovered.',
        updated
    ) % {'count': updated,
         'model': modeladmin.opts.verbose_name,
         'models': modeladmin.opts.verbose_name_plural,
         }

    modeladmin.message_user(
        request,
        message,
        messages.SUCCESS
    )


class IsDeletedAdminFilter(admin.SimpleListFilter):
    title = 'Deleted'
    parameter_name = 'is_deleted'

    def lookups(self, request, model_admin):
        return (
            (1, 'Yes',),
            (0, 'No'),
        )

    def queryset(self, request, queryset):
        if self.value() == '1':
            return queryset.filter(deleted_at__isnull=False)
        elif self.value() == '0':
            return queryset.filter(deleted_at__isnull=True)
        return queryset


class BaseAdminModel(admin.ModelAdmin):
    soft_delete = False
    save_on_top = True

    actions = (
        make_object_deleted_at,
        recover_object,
    )

    list_filter = (IsDeletedAdminFilter,)

    formfield_overrides = {
        PhoneNumberField: {'widget': PhoneNumberPrefixWidget},
    }

    readonly_fields = ('created_at', 'updated_at',)

    def get_fieldsets(
            self: DjangoModelAdminProtocol,
            request: HttpRequest,
            obj: Type[models.Model] | None = None
    ) -> Any:
        if (not obj and hasattr(self, 'add_fieldsets')
                and self.add_fieldsets is not None):
            return self.add_fieldsets

        return super().get_fieldsets(request, obj)  # type: ignore

    def has_delete_permission(
            self,
            request: HttpRequest,
            obj: Type[models.Model] | None = None
    ):
        return not bool(self.soft_delete)
