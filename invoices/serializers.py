from rest_framework import serializers
from .models import Invoice
from contracts.serializers import DetailedContractSerializer
from employees.serializers import EmployeeSerializer


class InvoiceSerializer(serializers.ModelSerializer):
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
            "employee_id",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]

    def create(self, validated_data):
        return Invoice.objects.create(**validated_data)


class DetailedInvoiceSerializer(serializers.ModelSerializer):
    contract = DetailedContractSerializer(read_only=True)
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
            "employee",
        ]

        read_only_fields = ["id", "created_at", "contract", "employee"]
