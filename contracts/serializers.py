from rest_framework import serializers
from .models import Contract

from categories.serializers import CategorySerializer

from suppliers.serializers import SupplierSerializer


class ContractSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Contract
        fields = ["id", "duration", "value", "category_id", "category", "supplier"]
        read_only_fields = ["id", "category", "supplier"]

    def create(self, validated_data):
        return Contract.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance


class DetailedContractSerializer(serializers.ModelSerializer):
    invoice_count = serializers.SerializerMethodField()
    category = CategorySerializer(read_only=True)
    supplier = SupplierSerializer(read_only=True)

    def get_invoice_count(self, obj: Contract):
        return obj.invoices.count()

    class Meta:
        model = Contract
        fields = ["id", "duration", "value", "invoice_count", "category", "supplier"]

        read_only_fields = ["id", "supplier"]
