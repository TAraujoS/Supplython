from rest_framework import serializers
from .models import Invoice
from rest_framework.validators import UniqueValidator
from contracts.serializers import ContractSerializer
from suppliers.serializers import SupplierSerializer
from employees.serializers import EmployeeSerializer


class InvoiceSerializer(serializers.ModelSerializer):
    invoice_number = serializers.CharField(
        validators=[
            UniqueValidator(Invoice.objects.all(), "Invoice Number should be unique.")
        ],
    )

    class Meta:
        model = Invoice
        fields = [
            "id",
            "invoice_number",
            "value",
            "description",
            "verified",
            "created_at",
            "validity",
            "contract_id",
            "supplier_id",
            "employee_id",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]

    def create(self, validated_data):
        return Invoice.objects.create(**validated_data)


class DetailedInvoiceSerializer(serializers.ModelSerializer):
    contract = ContractSerializer(read_only=True)
    supplier = SupplierSerializer(read_only=True)
    employee = EmployeeSerializer(read_only=True)

    class Meta:
        model = Invoice
        fields = [
            "id",
            "invoice_number",
            "value",
            "description",
            "verified",
            "created_at",
            "validity",
            "contract",
            "supplier",
            "employee",
        ]

        read_only_fields = ["id", "created_at", "contract", "supplier", "employee"]
