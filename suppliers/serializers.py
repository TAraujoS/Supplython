from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import Supplier
from contracts.models import Contract
from rest_framework.validators import UniqueValidator
from .new_serializer import (
    ContractNewSerializer,
    DepartmentNewSerializer,
)


class SupplierSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        validators=[UniqueValidator(Supplier.objects.all(), "Name should be unique.")],
    )

    email = serializers.EmailField(
        validators=[
            UniqueValidator(Supplier.objects.all(), "E-mail should be unique.")
        ],
        max_length=50,
    )

    tel = serializers.CharField(
        validators=[
            UniqueValidator(Supplier.objects.all(), "Contact should be unique.")
        ],
        max_length=20,
    )

    class Meta:
        model = Supplier
        fields = [
            "id",
            "name",
            "email",
            "tel",
            "cnpj",
        ]

        read_only_fields = ["id"]

    def create(self, validated_data):
        return Supplier.objects.create(**validated_data)


class SupplierDetailSerializer(serializers.ModelSerializer):
    
    contracts = ContractNewSerializer(read_only=True, many=True)
    departments = DepartmentNewSerializer(read_only=True, many=True)
    contract_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Supplier
        fields = [
            "id",
            "name",
            "email",
            "tel",
            "cnpj",
            "contracts",
            "departments",
            "contract_id",
        ]

        read_only_fields = [
            "id",
            "contracts",
            "departments",
        ]

    def update(self, instance: Supplier, validated_data: dict) -> Supplier:
        contract = validated_data.pop("contract_id", None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        find_contract = get_object_or_404(Contract, pk=contract)

        if contract:
            instance.contracts.add(find_contract)

        instance.save()

        return instance
