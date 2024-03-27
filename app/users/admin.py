from django.contrib import admin

from app.core.admin import BaseAdminModel
from app.users.models import User


@admin.register(User)
class UserAdmin(BaseAdminModel):
    soft_delete = True

    list_display = (
        'id',
        'email',
    )

    readonly_fields = (
        'date_joined',
        'last_login',
        'updated_at',
    )

    search_fields = ('first_name', 'last_name', 'email')
    search_help_text = 'Fiend by first / last names, email'

    fieldsets = (
        (None,
         {
             'classes': ['extrapretty'],
             'fields': (
                 'is_staff',
                 'is_superuser',
             )
         }),
        ('General',
         {
             'classes': ['extrapretty'],
             'fields':
                 (
                     (
                         'email',
                         'phone'
                     ),
                     (
                         'first_name',
                         'last_name',
                         'patronymic',
                     ),
                 ),
         }),
        ('Permissions',
         {
             'classes': ['collapse'],
             'fields': (
                 'groups',
                 'user_permissions',
             ),
         }),
        ('Dates',
         {
             'fields': (
                 'date_joined',
                 'last_login',
                 'updated_at',
                 'deleted_at',
             )
         }),
    )

    add_fieldsets = (
        (None,
         {
             'classes': ['extrapretty'],
             'fields': (
                 'is_staff',
                 'is_superuser',
             )}),
        ('General',
         {
             'classes': ['extrapretty'],
             'fields':
                 (
                     (
                         'email',
                         'phone',
                     ),
                     (
                         'first_name',
                         'last_name',
                         'patronymic',
                     ),
                 ),
         }),
        ('Permissions',
         {
             'classes': ['collapse'],
             'fields': (
                 'groups',
                 'user_permissions',
             ),
         }),
    )

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return self.fieldsets
