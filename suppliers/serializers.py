from rest_framework import serializers
from .models import Supplier
from rest_framework.validators import UniqueValidator
from .newSerialier import (
    ContractNewSerializer,
    CategoryNewSerializer,
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
    categories = CategoryNewSerializer(read_only=True, many=True)
    departments = DepartmentNewSerializer(read_only=True, many=True)
    category_id = serializers.IntegerField(write_only=True)
    department_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Supplier
        fields = [
            "id",
            "name",
            "email",
            "tel",
            "cnpj",
            "contracts",
            "categories",
            "departments",
            "category_id",
            "department_id",
        ]

        read_only_fields = [
            "id",
            "name",
            "email",
            "tel",
            "cnpj",
            "contracts",
            "categories",
            "departments",
        ]

        def update(self, instance: Supplier, validated_data: dict) -> Supplier:
            # department = validated_data.pop("department_id")
            # category = validated_data.pop("category_id")

            for key, value in validated_data.items():
                setattr(instance, key, value)

            # if category:
            #     instance.categories.add(category)

            # if department:
            #     instance.departments.add(department)
            instance.save()
            # instance.supplier.add(category, department)

            return instance
