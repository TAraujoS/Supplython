from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_spectacular.utils import extend_schema_view, extend_schema
from django.shortcuts import get_object_or_404

from .models import Supplier
from .serializers import SupplierSerializer, SupplierDetailSerializer
from employees.permissions import IsManager


@extend_schema_view(
    post=extend_schema(
        description="Route to create Suppliers. Route only for managers",
        summary="Create Supplier",
        tags=["Suppliers"],
    ),
    get=extend_schema(
        description="Route to list all Suppliers. Route only for managers",
        summary="List all Suppliers",
        tags=["Suppliers"],
    ),
)
class SupplierView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManager]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return SupplierDetailSerializer

        return SupplierSerializer

    queryset = Supplier.objects.all()


@extend_schema_view(
    get=extend_schema(
        description="Route to list Supplier by id. Route only for managers",
        summary="List Supplier by id",
        tags=["Suppliers"],
    ),
    patch=extend_schema(
        description="Route to update Supplier by id. Route only for managers",
        summary="Update Supplier",
        tags=["Suppliers"],
    ),
    delete=extend_schema(
        description="Route to delete Supplier by id. Route only for managers",
        summary="Delete Supplier",
        tags=["Suppliers"],
    ),
    put=extend_schema(exclude=True),
)
class SupplierDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManager]

    serializer_class = SupplierDetailSerializer
    queryset = Supplier.objects.all()
