from rest_framework import serializers
from .models import Supplier
from rest_framework.validators import UniqueValidator
from .newSerialier import (
    ContractNewSerializer,
    DepartmentNewSerializer,
)
from django.shortcuts import get_object_or_404
from contracts.models import Contract


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
    # categories = CategoryNewSerializer(read_only=True, many=True)
    departments = DepartmentNewSerializer(read_only=True, many=True)
    # category_id = serializers.IntegerField(write_only=True)
    # department_id = serializers.IntegerField(write_only=True)
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
            # "categories",
            "departments",
            # "category_id",
            # "department_id",
            "contract_id",
        ]

        read_only_fields = [
            "id",
            "contracts",
            # "categories",
            "departments",
        ]

    def update(self, instance: Supplier, validated_data: dict) -> Supplier:
        # department = validated_data.pop("department_id", None)
        # category = validated_data.pop("category_id", None)
        contract = validated_data.pop("contract_id", None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        find_contract = get_object_or_404(Contract, pk=contract)

        if contract:
            instance.contracts.add(find_contract)

        instance.save()

        return instance
