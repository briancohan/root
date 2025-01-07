from typing import Any

from django.core.handlers.wsgi import WSGIRequest
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request: WSGIRequest, view: Any, obj: Any) -> bool:  # noqa: ANN401
        print(type(view))
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
