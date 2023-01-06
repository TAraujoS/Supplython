from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Contract
from categories.models import Category
from suppliers.models import Supplier
from .serializers import ContractSerializer, DetailedContractSerializer
from employees.permissions import IsManager
from django.shortcuts import get_object_or_404


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


class ContractDetailView(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classe = [IsManager]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return DetailedContractSerializer

        return ContractSerializer

    queryset = Contract.objects.all()
