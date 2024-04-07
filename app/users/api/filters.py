from django_filters import rest_framework as rf


class ClientSubscriptionFilter(rf.FilterSet):
    is_active = rf.BooleanFilter(field_name='is_active')
    is_deleted = rf.BooleanFilter(
        method='is_deleted_filter',
        field_name='deleted_at'
    )

    def is_deleted_filter(self, queryset, name, value):
        if value:
            return queryset.filter(deleted_at__isnull=False)
        return queryset.filter(deleted_at__isnull=True)
