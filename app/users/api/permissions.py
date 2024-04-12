from typing import Any

from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.views import APIView


class IsOwner(IsAuthenticated):
    def has_object_permission(
            self,
            request: Request,
            view: APIView,
            obj: Any
    ) -> bool:
        return request.user == obj
