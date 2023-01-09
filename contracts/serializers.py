from rest_framework import serializers
from .models import Contract

from suppliers.serializers import SupplierSerializer
from categories.serializers import CategorySerializer
from invoices.models import Invoice
from invoices.serializers import InvoiceSerializer


class ContractSerializer(serializers.ModelSerializer):
    invoice_count = serializers.SerializerMethodField()

    def get_invoice_count(self, obj: Contract):
        invoice_list = Contract.objects.get(id=obj.id).Invoice.all()

        result = invoice_list.count()

        return result

    class Meta:
        model = Contract
        fields = [
            "id",
            "duration",
            "value",
            "invoice_list",
            "supplier_id",
            "category_id",
        ]
        read_only_fields = ["id"]

    def create(self, validated_data):
        return Contract.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance


class DetailedContractSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    supplier = SupplierSerializer(read_only=True)

    class Meta:
        model = Contract
        fields = [
            "id",
            "duration",
            "value",
            "category",
            "supplier",
        ]

        read_only_fields = ["id", "duration", "value", "category", "supplier"]
