from rest_framework import serializers
from .models import Category
from suppliers.serializers import SupplierSerializer


class CategorySerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = ["id", "name", "supplier"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        supplier_list = validated_data.pop("supplier")

        category = Category.objects.create(**validated_data)

        category.supplier.add(supplier_list)

        return category
