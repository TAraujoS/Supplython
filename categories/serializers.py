from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]
        read_only_fields = ["id"]


class DetailCategorySerializer(serializers.ModelSerializer):
    supplier_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "supplier_id"]
        read_only_fields = ["id"]

    def update(self, instance: Category, validated_data: dict) -> Category:
        supplier = validated_data.pop("supplier_id")

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.supplier.add(supplier)

        return instance
