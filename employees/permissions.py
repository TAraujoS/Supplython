from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Employee


class isAdminOrAccountOwner(permissions.BasePermission):
    def has_object_permission(
        self, request: Request, view: View, obj: Employee
    ) -> bool:

        if request.employee.is_authenticated and (
            request.employee == obj or request.employee.is_superuser
        ):
            return True

        return False
