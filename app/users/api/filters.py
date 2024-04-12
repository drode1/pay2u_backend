from typing import Any

from django.db.models import QuerySet
from django_filters import rest_framework as rf


class ClientSubscriptionFilter(rf.FilterSet):
    is_active = rf.BooleanFilter(field_name='is_active')
    is_deleted = rf.BooleanFilter(
        method='is_deleted_filter',
        field_name='deleted_at'
    )

    def is_deleted_filter(
            self,
            queryset: QuerySet,
            name: Any,
            value: str
    ) -> QuerySet:
        if value:
            return queryset.filter(deleted_at__isnull=False)
        return queryset.filter(deleted_at__isnull=True)
