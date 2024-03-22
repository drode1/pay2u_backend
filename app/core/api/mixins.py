from rest_framework import mixins, status
from rest_framework.response import Response


class CreateModelMixin(mixins.CreateModelMixin):
    """
    Create a model instance.
    """

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        if self.response_serializer_class:
            serialized_data = self.response_serializer_class(serializer.instance).data  # noqa: E501
        else:
            serialized_data = serializer.data

        return Response(serialized_data, status=status.HTTP_201_CREATED, headers=headers)  # noqa: E501


class UpdateModelMixin:
    """
    Update a model instance.
    """

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)  # noqa: E501
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        if self.response_serializer_class:
            serialized_data = self.response_serializer_class(serializer.instance).data  # noqa: E501
        else:
            serialized_data = serializer.data

        return Response(serialized_data, status=status.HTTP_200_OK)


class SoftDestroyModelMixin:
    """
    Soft destroy a model instance.
    """

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.soft_delete()
        return instance


class RecoverModelMixin:
    """
    Recover a model instance.
    """

    def recover(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_recover(instance)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def perform_recover(self, instance):
        instance.recover()
        return instance
