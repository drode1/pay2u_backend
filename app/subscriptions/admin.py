from django.contrib import admin

from app.core.admin import BaseAdminModel
from app.subscriptions.models import (
    Cashback,
    Category,
    Invoice,
    Promocode,
    Subscription,
    Tariff,
)


@admin.register(Category)
class CategoryAdmin(BaseAdminModel):
    list_display = (
        'id',
        'name',
    )
    search_fields = (
        'name',
    )
    search_help_text = f"Find by {' / '.join(search_fields)}"
    fieldsets = (
        (
            'General', {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'name',
                ),
            }
        ),
        (
            'Additional Information', {
                'fields': (
                    'created_at',
                    'updated_at',
                    'deleted_at'
                ),
            }
        ),
    )


@admin.register(Cashback)
class CashbackAdmin(BaseAdminModel):
    list_display = (
        'id',
        'amount',
    )

    search_fields = (
        'amount',
    )
    search_help_text = f"Find by {' / '.join(search_fields)}"
    fieldsets = (
        (
            'General', {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'amount',
                ),
            }
        ),
        (
            'Additional Information', {
                'fields': (
                    'created_at',
                    'updated_at',
                    'deleted_at'
                ),
            }
        ),
    )


@admin.register(Invoice)
class InvoiceAdmin(BaseAdminModel):
    list_display = (
        'id',
        'amount',
    )
    readonly_fields = (
        'date',
        'amount',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'amount',
    )
    search_help_text = f"Find by {' / '.join(search_fields)}"
    fieldsets = (
        (
            'General', {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'amount',
                    'date',
                ),
            }
        ),
        (
            'Additional Information', {
                'fields': (
                    'created_at',
                    'updated_at',
                    'deleted_at'
                ),
            }
        ),
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Promocode)
class PromocodeAdmin(BaseAdminModel):
    list_display = (
        'id',
        'name',
        'amount',
        'is_active',
    )
    list_filter = (
        'is_active',
    )
    search_fields = (
        'name',
        'amount',
    )
    search_help_text = f"Find by {' / '.join(search_fields)}"
    fieldsets = (
        (
            'General', {
                'classes': (
                    'pretty',
                ),
                'fields': (
                    'is_active',
                    'name',
                    'amount',
                ),
            }
        ),
        (
            'Additional Information', {
                'fields': (
                    'created_at',
                    'updated_at',
                    'deleted_at'
                ),
            }
        ),
    )


class TariffInlineUserAdmin(admin.TabularInline):
    model = Tariff
    extra = -1
    fk_name = 'subscription'
    min_num = 1
    max_num = 5


@admin.register(Subscription)
class SubscriptionAdmin(BaseAdminModel):
    list_display = (
        'id',
        'name',
        'cashback',
        'category',
        'is_recommended',
    )
    list_filter = (
        'is_recommended',
    )
    search_fields = (
        'name',
        'category',
    )
    search_help_text = f"Find by {' / '.join(search_fields)}"
    inlines = [
        TariffInlineUserAdmin,
    ]
    fieldsets = (
        (
            'General', {
                'classes': (
                    'pretty',
                ),
                'fields': (
                    'is_recommended',
                    (
                        'name',
                        'description',
                    ),
                    'image',
                    (
                        'cashback',
                        'category',
                    ),
                )
            }
        ),
        (
            'Additional Information', {
                'fields': (
                    'created_at',
                    'updated_at',
                    'deleted_at'
                ),
            }
        ),
    )


@admin.register(Tariff)
class TariffAdmin(BaseAdminModel):
    list_display = (
        'id',
        'name',
        'subscription',
        'promocode',
        'amount',
    )
    search_fields = (
        'name',
        'subscription',
        'promocode',
    )
    search_help_text = f"Find by {' / '.join(search_fields)}"
    fieldsets = (
        (
            'General', {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'amount',
                    (
                        'name',
                        'description',
                    ),
                    (
                        'subscription',
                        'promocode',
                    ),
                )
            }
        ),
        (
            'Additional Information', {
                'fields': (
                    'created_at',
                    'updated_at',
                    'deleted_at'
                ),
            }
        ),
    )
