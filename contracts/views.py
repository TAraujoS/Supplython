from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Contract
from categories.models import Category
from suppliers.models import Supplier
from .serializers import ContractSerializer
from employees.permissions import IsManager
from django.shortcuts import get_object_or_404


class ContractView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classe = [IsManager]

    serializer_class = ContractSerializer
    queryset = Contract.objects.all()


def perform_create(self, serializer):
    categories = get_object_or_404(Category, pk=self.kwargs["pk"])
    return serializer.save(categories=categories)


class ContractDetailView(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classe = [IsManager]

    serializer_class = ContractSerializer
    queryset = Contract.objects.all()

    def perform_create(self, serializer):
        supplier = get_object_or_404(Supplier, pk=self.kwargs["pk"])
        return serializer.save(supplier=supplier)
