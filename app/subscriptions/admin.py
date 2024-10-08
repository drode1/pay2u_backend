from django.contrib import admin
from django.http import HttpRequest

from app.core.admin import BaseAdminModel, IsDeletedAdminFilter
from app.subscriptions.models import (
    Cashback,
    Category,
    ClientSubscription,
    Invoice,
    Promocode,
    Subscription,
    SubscriptionBenefits,
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

    def has_change_permission(
            self,
            request: HttpRequest,
            obj: Invoice | None = None
    ) -> bool:
        return False

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def has_delete_permission(
            self,
            request: HttpRequest,
            obj: Invoice | None = None
    ) -> bool:
        return False


@admin.register(Promocode)
class PromocodeAdmin(BaseAdminModel):
    soft_delete = True
    list_display = (
        'id',
        'name',
        'is_active',
    )
    list_filter = (
        'is_active',
    )
    search_fields = (
        'name',
    )
    search_help_text = f"Find by {' / '.join(search_fields)}"
    fieldsets = (
        (
            'General', {
                'classes': (
                    'extrapretty',
                ),
                'fields': (
                    'is_active',
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

    def has_change_permission(
            self,
            request: HttpRequest,
            obj: Promocode | None = None
    ) -> bool:
        return False

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False


class TariffInlineUserAdmin(admin.TabularInline):
    model = Tariff
    extra = 0
    fk_name = 'subscription'
    min_num = 1


class BenefitsInlineUserAdmin(admin.TabularInline):
    model = SubscriptionBenefits
    extra = 0
    min_num = 0
    max_num = 5
    fields = ('icon', 'benefit',)


@admin.register(Subscription)
class SubscriptionAdmin(BaseAdminModel):
    soft_delete = True
    list_display = (
        'id',
        'name',
        'cashback',
        'category',
        'is_recommended',
    )
    list_filter = (
        'is_recommended',
        IsDeletedAdminFilter,
    )
    search_fields = (
        'name',
        'category',
    )
    search_help_text = f"Find by {' / '.join(search_fields)}"
    inlines = (
        TariffInlineUserAdmin,
        BenefitsInlineUserAdmin,
    )
    fieldsets = (
        (
            'General', {
                'classes': (
                    'extrapretty',
                ),
                'fields': (
                    'is_recommended',
                    (
                        'popularity',
                        'name',
                        'description',
                        'conditions',
                    ),
                    'image_preview',
                    'image_detail',
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
    soft_delete = True
    list_display = (
        'id',
        'days_amount',
        'subscription',
        'amount',
    )
    list_filter = (
        'subscription',
    )
    search_fields = (
        'subscription',
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
                        'days_amount',
                        'description',
                    ),
                    (
                        'subscription',
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


@admin.register(ClientSubscription)
class ClientSubscriptionAdmin(BaseAdminModel):
    soft_delete = True
    list_display = (
        'id',
        'client',
        'subscription',
        'tariff',
        'expiration_date',
        'is_auto_pay',
    )
    list_filter = (
        'is_active',
        'is_auto_pay',
    )
    search_fields = (
        'client__email',
        'subscription__name',
        'tariff__name',
    )
    readonly_fields = (
        'is_active',
        'client',
        'subscription',
        'tariff',
        'promocode',
        'invoice',
        'expiration_date',
        'created_at',
        'updated_at',
    )
    search_help_text = f"Find by {' / '.join(search_fields)}"
    fieldsets = (
        (
            None, {
                'fields': (
                    'is_active',
                    'is_auto_pay',
                )
            }
        ),
        (
            'General', {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'client',
                    'subscription',
                    'tariff',
                )
            }
        ),
        (
            'Payment data', {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'promocode',
                    'invoice',
                    'expiration_date',
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

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False
