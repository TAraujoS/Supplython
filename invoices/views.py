from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema_view, extend_schema

from .models import Invoice
from .serializers import InvoiceSerializer, DetailedInvoiceSerializer
from employees.permissions import IsManager
from contracts.models import Contract
from employees.models import Employee
from utils.factory_pdf import factory_pdf


@extend_schema_view(
    post=extend_schema(
        description="Route to create Invoice.",
        summary="Create Invoice",
        tags=["Invoices"],
    ),
    get=extend_schema(
        description="Route to list all Invoices.",
        summary="List all Invoices.",
        tags=["Invoices"],
    ),
)
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
            if invoices_verify[0].contract_id == self.request.data["contract_id"]:
                raise ValidationError(
                    {"details": "This note has already been released."}
                )

        contract = get_object_or_404(Contract, id=self.request.data["contract_id"])
        employee = get_object_or_404(Employee, id=self.request.data["employee_id"])

        factory_pdf(self.request.data, contract, employee)

        return serializer.save(
            contract=contract,
            employee=employee,
        )


@extend_schema_view(
    get=extend_schema(
        description="Route to list Invoice by id. Route only for managers",
        summary="List Invoice by id",
        tags=["Invoices"],
    ),
    patch=extend_schema(
        description="Route to update Invoice by id. Route only for managers",
        summary="Update Invoice",
        tags=["Invoices"],
    ),
    delete=extend_schema(
        description="Route to delete Invoice by id. Route only for managers",
        summary="Delete Invoice.",
        tags=["Invoices"],
    ),
    put=extend_schema(exclude=True),
)
class InvoiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManager]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return DetailedInvoiceSerializer

        return InvoiceSerializer

    queryset = Invoice.objects.all()
