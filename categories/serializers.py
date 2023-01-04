from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]  # "supplier_id" "contract_id"
        read_only_fields = ["id"]
