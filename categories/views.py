from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema_view, extend_schema

from .models import Category
from .serializers import CategorySerializer, DetailCategorySerializer
from suppliers.models import Supplier
from employees.permissions import IsManager


@extend_schema_view(
    post=extend_schema(
        description="Route to create Categories. Route only for managers",
        summary="Create Categories",
        tags=["Categories"],
    ),
    get=extend_schema(
        description="Route to list all Categories. Route only for managers",
        summary="List all Categories",
        tags=["Categories"],
    ),
)
class CategoryView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManager]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        supplier = get_object_or_404(Supplier, id=self.request.data["supplier_id"])

        return serializer.save(supplier=supplier)


@extend_schema_view(
    get=extend_schema(
        description="Route to list Category by id. Route only for managers",
        summary="List Category by id",
        tags=["Categories"],
    ),
    patch=extend_schema(
        description="Route to update Category. Route only for managers",
        summary="Update Category",
        tags=["Categories"],
    ),
    delete=extend_schema(
        description="Route to delete Category by id. Route only for managers",
        summary="Delete Category",
        tags=["Categories"],
    ),
    put=extend_schema(exclude=True),
)
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManager]

    queryset = Category.objects.all()
    serializer_class = DetailCategorySerializer
