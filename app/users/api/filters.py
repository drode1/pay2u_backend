from django_filters import rest_framework as rf


class IsDeletedFilter(rf.FilterSet):
    is_deleted = rf.BooleanFilter(
        method='is_deleted_filter',
        field_name='deleted_at'
    )

    def is_deleted_filter(self, queryset, name, value):
        if value:
            return queryset.filter(deleted_at__isnull=False)
        return queryset.filter(deleted_at__isnull=True)
