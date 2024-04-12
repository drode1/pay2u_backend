from django.core.exceptions import ObjectDoesNotExist
from rest_framework.relations import PrimaryKeyRelatedField


class IdRelatedFieldSerializer(PrimaryKeyRelatedField):
    """
    Basic PK serializer, but in which method is rewritten to_internal_value method,
    so that in the browser interface of DRF the Foreign Key ID of the model was correctly left.
    Foreign Key ID of the model.
    """

    def to_internal_value(self, data):
        if self.pk_field is not None:
            data = self.pk_field.to_internal_value(data)
        queryset = self.get_queryset()
        try:
            if isinstance(data, bool):
                raise TypeError  # noqa: TRY301
            return queryset.get(pk=data).pk
        except ObjectDoesNotExist:
            self.fail('does_not_exist', pk_value=data)
        except (TypeError, ValueError):
            self.fail('incorrect_type', data_type=type(data).__name__)
