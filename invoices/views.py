from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
from .serializers import InvoiceSerializer, DetailedInvoiceSerializer
from .models import Invoice
from employees.permissions import IsManager
from contracts.models import Contract
from employees.models import Employee
from suppliers.models import Supplier
from django.shortcuts import get_object_or_404
import ipdb


class InvoiceView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return DetailedInvoiceSerializer

        return InvoiceSerializer

    queryset = Invoice.objects.all()

    def perform_create(self, serializer):

        contract = get_object_or_404(Contract, id=self.request.data["contract_id"])
        supplier = get_object_or_404(Supplier, id=self.request.data["supplier_id"])
        employee = get_object_or_404(Employee, id=self.request.data["employee_id"])

        return serializer.save(
            contract=contract,
            supplier=supplier,
            employee=employee,
        )


class InvoiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManager]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return DetailedInvoiceSerializer

        return InvoiceSerializer

    queryset = Invoice.objects.all()
