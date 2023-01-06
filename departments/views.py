from rest_framework import generics
from .serializer import DepartmentSerializer
from .models import Department
from rest_framework_simplejwt.authentication import JWTAuthentication
from employees.permissions import IsManager
from django.shortcuts import get_object_or_404
from suppliers.models import Supplier
from drf_spectacular.utils import extend_schema_view, extend_schema


@extend_schema_view(
    post = extend_schema(
        description= "Route to create Department.Route only for managers",
        summary= "Create a Department",
        tags=["Departments"]
    ),
    get=extend_schema(
        description= "Route to list all Departments.Route only for managers",
        summary= "List all Departments",
        tags=["Departments"]
    ),
)


class DepartmentView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManager]

    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

    def perform_create(self, serializer):
        supplier = get_object_or_404(Supplier, id=self.request.data["supplier"])

        return serializer.save(supplier=supplier)


class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManager]

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
