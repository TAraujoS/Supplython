from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Employee
import ipdb


class IsManager(permissions.BasePermission):
    def has_object_permission(
        self, request: Request, view: View, obj: Employee
    ) -> bool:

        if request.user.is_authenticated and request.user.is_manager:

            return True

        return False


class isAdminGet(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:

        if request.method == "GET" and request.user.is_manager:

            return True

        if request.method == "POST":

            return True

        return False
