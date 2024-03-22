from django.contrib import admin, messages
from django.db import models
from django.utils.timezone import now
from django.utils.translation import ngettext
from django_json_widget.widgets import JSONEditorWidget


@admin.action(description='Delete')
def make_object_deleted_at(modeladmin, request, queryset):
    updated = queryset.update(deleted_at=now())

    message = ngettext(
        "%(count)d %(model)s was deleted.",
        "%(count)d %(models)s were deleted.",
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
        "%(count)d %(model)s was recovered.",
        "%(count)d %(models)s were recovered.",
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


class BaseAdminModel(admin.ModelAdmin):
    soft_delete = False
    save_on_top = True

    actions = (
        make_object_deleted_at,
        recover_object,
    )

    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }

    readonly_fields = ('created_at', 'updated_at',)

    def has_delete_permission(self, request, obj=None):
        return False if self.soft_delete else True
