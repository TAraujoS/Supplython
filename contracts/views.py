from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema_view, extend_schema

from .models import Contract
from categories.models import Category
from .serializers import ContractSerializer, DetailedContractSerializer
from employees.permissions import IsManager


@extend_schema_view(
    post=extend_schema(
        description="Route to create Contracts. Route only for managers.",
        summary="Create Contracts",
        tags=["Contracts"],
    ),
    get=extend_schema(
        description="Route to list all contracts. Route only for managers.",
        summary="List all Contracts.",
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

        return serializer.save(category=categories)


@extend_schema_view(
    get=extend_schema(
        description="Route to list Contract by id. Route only for managers",
        summary="List Contract by id",
        tags=["Contracts"],
    ),
    patch=extend_schema(
        description="Route to update Contract by id. Route only for managers",
        summary="Update Contract",
        tags=["Contracts"],
    ),
    delete=extend_schema(
        description="Route to delete Contract by id. Route only for managers",
        summary="Delete Contract.",
        tags=["Contracts"],
    ),
    put=extend_schema(exclude=True),
)
class ContractDetailView(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classe = [IsManager]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return DetailedContractSerializer

        return ContractSerializer

    queryset = Contract.objects.all()
