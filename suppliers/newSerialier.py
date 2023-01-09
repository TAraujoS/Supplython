from contracts.models import Contract
from categories.models import Category
from departments.models import Department
from rest_framework import serializers

class ContractNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = [
            "id",
            "duration",
            "value",
        ]
        read_only_fields = ['id']




class CategoryNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

        read_only_fields = ['id']
    


class DepartmentNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["id", "name", "budget"]

        read_only_fields = ['id']
    