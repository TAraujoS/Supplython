from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema_view, extend_schema


from .models import Contract
from categories.models import Category
from suppliers.models import Supplier
from .serializers import ContractSerializer, DetailedContractSerializer
from employees.permissions import IsManager


@extend_schema_view(
    post=extend_schema(
        description="Route to create Contracts. Route only for managers.",
        summary="Create contract",
        tags=["Contracts"],
    ),
    get=extend_schema(
        description="Route for an authenticated user to list all contracts.",
        summary="List all contracts.",
        tags=["Contracts"],
    ),
)
class ContractView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classe = [IsManager]

    queryset = Contract.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return DetailedContractSerializer

        return ContractSerializer

    def perform_create(self, serializer):
        categories = get_object_or_404(Category, id=self.request.data["category_id"])
        supplier = get_object_or_404(Supplier, id=self.request.data["supplier_id"])
        return serializer.save(category=categories, supplier=supplier)


get = (
    extend_schema(
        description="Route for an authenticated and manager to list a specific contract by id.",
        summary="List contract",
        tags=["Contracts"],
    ),
)


class ContractDetailView(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classe = [IsManager]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return DetailedContractSerializer

        return ContractSerializer

    queryset = Contract.objects.all()
