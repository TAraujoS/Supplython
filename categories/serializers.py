from rest_framework import serializers
from .models import Category

# from suppliers.serializers import SupplierSerializer
# from contracts.serializers import ContractSerializer


class CategorySerializer(serializers.ModelSerializer):
    # contract = ContractSerializer(read_only=True, many=True)
    # supplier = SupplierSerializer(read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        return Category.objects.create(**validated_data)
