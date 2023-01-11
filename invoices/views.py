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
from suppliers.models import Supplier
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from .models import Invoice
from django.core.mail import  EmailMessage #send_mail,
from django.conf import settings
from fpdf import FPDF
import ipdb


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
        # data_pdf = Invoice.objects.all() #lista
        # ipdb.set_trace()

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("helvetica", "", 14)
        pdf.multi_cell(txt="Supplython Invoices", h=1, align= "C", w=0)
        pdf.ln(10)
        # pdf.multi_cell(txt=f"ID {self.request.data['id']}", w=0)
        pdf.ln(2)
        pdf.multi_cell(txt=f"INVOICE_NUMBER = {self.request.data['invoice_number']}", w=0)
        pdf.ln(2)
        pdf.multi_cell(txt=f"VALUE = {self.request.data['value']}", w=0)
        pdf.ln(2)
        pdf.multi_cell(txt=f"DESCRIPTION = {self.request.data['description']}", w=0)
        pdf.ln(2)
        pdf.multi_cell(txt=f"CONTRACT = {contract}", w=0)
        pdf.ln(2)
        pdf.multi_cell(txt=f"VALIDITY = {self.request.data['validity']}", w=0)
        pdf.ln(2)

        # for item in data_pdf:
        #     pdf.multi_cell(txt=f"{item}", w=0 )
        
        pdf.output("invoice.pdf")
        
        email = EmailMessage(
            subject= "New Invoice Created",
            body= "A new invoice was generated in the name of your company, check the data that were filled in !",
            from_email=settings.EMAIL_HOST_USER,
            to=[contract.supplier.email],
            
        )
        email.attach_file("invoice.pdf")
        email.send(fail_silently=False)

        

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
