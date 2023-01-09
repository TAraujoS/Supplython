from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Department
from suppliers.serializers import SupplierSerializer


class DepartmentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        validators=[
            UniqueValidator(Department.objects.all(), "Name should be unique.")
        ],
    )
    supplier = SupplierSerializer(read_only=True, many=True)

    class Meta:
        model = Department
        fields = ["id", "name", "budget", "supplier"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        supplier_list = validated_data.pop("supplier")

        department = Department.objects.create(**validated_data)

        department.supplier.add(supplier_list)

        return department

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance
