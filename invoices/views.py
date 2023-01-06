from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import InvoiceSerializer, DetailedInvoiceSerializer
from django.shortcuts import get_object_or_404
from employees.permissions import IsManager
from contracts.models import Contract
from employees.models import Employee
from suppliers.models import Supplier
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from .models import Invoice


class InvoiceView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return DetailedInvoiceSerializer

        return InvoiceSerializer

    queryset = Invoice.objects.all()

    def perform_create(self, serializer):

        invoices_verify = Invoice.objects.filter(
            invoice_number=self.request.data["invoice_number"]
        )

        if len(invoices_verify) > 0:
            if invoices_verify[0].supplier_id == self.request.data["supplier_id"]:
                raise ValidationError(
                    {"details": "This note has already been released."}
                )

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
