from .models import Supplier
from .serializers import SupplierSerializer, SupplierDetailSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from employees.permissions import IsManager
from drf_spectacular.utils import extend_schema_view, extend_schema


@extend_schema_view(
    post=extend_schema(
        description="Route to create suppliers",
        summary="Create Supplier",
        tags=["Suppliers"],
    ),
    get=extend_schema(
        description="Route for a manager to list all suppliers",
        summary="List all suppliers",
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
        description="Route for a manager to list a single supplier",
        summary="List supplier",
        tags=["Suppliers"],
    ),
    patch=extend_schema(
        description="Route for a manager to update a supplier",
        summary="Update supplier",
        tags=["Suppliers"],
    ),
)

    
class SupplierDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManager]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return SupplierDetailSerializer

        return SupplierSerializer

    queryset = Supplier.objects.all()
