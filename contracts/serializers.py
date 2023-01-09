from rest_framework import serializers
from .models import Contract

from categories.serializers import CategorySerializer


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = [
            "id",
            "duration",
            "value",
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
    invoice_count = serializers.SerializerMethodField()
    category = CategorySerializer(read_only=True)

    def get_invoice_count(self, obj: Contract):
        return obj.invoices.count()

    class Meta:
        model = Contract
        fields = [
            "id",
            "duration",
            "value",
            "invoice_count",
            "category",
        ]

        read_only_fields = ["id"]
