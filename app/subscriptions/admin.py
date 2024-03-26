from django.contrib import admin

from app.core.admin import BaseAdminModel
from app.subscriptions.models import Category, Cashback, Invoice


@admin.register(Category)
class CategoryAdmin(BaseAdminModel):
    list_display = (
        'id',
        'name',
    )

    search_fields = ('name',)
    search_help_text = 'Fiend by name'
    fieldsets = (
        ('General', {
            'classes': ('wide',),
            'fields': ('name',),
        }),
        ('Additional Information', {
            'fields': ('created_at', 'updated_at', 'deleted_at'),
        }),
    )


@admin.register(Cashback)
class CashbackAdmin(BaseAdminModel):
    list_display = (
        'id',
        'amount',
    )

    search_fields = ('amount',)
    search_help_text = 'Fiend by amount'
    fieldsets = (
        ('General', {
            'classes': ('wide',),
            'fields': ('amount',),
        }),
        ('Additional Information', {
            'fields': ('created_at', 'updated_at', 'deleted_at'),
        }),
    )


@admin.register(Invoice)
class InvoiceAdmin(BaseAdminModel):
    list_display = (
        'id',
        'amount',
    )
    readonly_fields = ('date', 'amount', 'created_at', 'updated_at',)
    search_fields = ('amount',)
    search_help_text = 'Fiend by amount'
    fieldsets = (
        ('General', {
            'classes': ('wide',),
            'fields': ('amount', 'date',),
        }),
        ('Additional Information', {
            'fields': ('created_at', 'updated_at', 'deleted_at'),
        }),
    )

    def has_add_permission(self, request):
        return False
