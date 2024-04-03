from rest_framework import generics
from rest_framework.exceptions import MethodNotAllowed

from app.core.api.mixins import (
    CreateModelMixin,
    RecoverModelMixin,
    SoftDestroyModelMixin,
    UpdateModelMixin,
)


class ListApiView(generics.ListAPIView):
    """ Abstract generic List API class """

    pass


class RetrieveApiView(generics.RetrieveAPIView):
    """ Abstract generic Retrieve API class """

    pass


class CreateApiView(CreateModelMixin, generics.CreateAPIView):
    """ Abstract generic Create API class """

    response_serializer_class = None


class UpdateApiView(UpdateModelMixin, generics.UpdateAPIView):
    """ Abstract generic Update API class """

    response_serializer_class = None

    def patch(self, request, *args, **kwargs):
        message = 'Partial updates are prohibited'
        raise MethodNotAllowed(method='PATCH', detail=message)


class DestroyApiView(generics.DestroyAPIView):
    """ Abstract generic Destroy API class """

    pass


class SoftDestroyApiView(SoftDestroyModelMixin, generics.GenericAPIView):
    """ Abstract generic Soft Destroy API class """

    response_serializer_class = None

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class RecoverApiView(RecoverModelMixin, generics.GenericAPIView):
    """ Abstract generic Recover API class """

    def get(self, request, *args, **kwargs):
        return self.recover(request, *args, **kwargs)
