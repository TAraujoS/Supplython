from rest_framework import serializers
from .models import Invoice


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
            "supplier_id",
            "employee_id",
        ]
        
        

        read_only_fields = [
            "id",
            "created_at",
        ]

    def create(self, validated_data):
        return Invoice.objects.create(**validated_data)
