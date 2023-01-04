from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        validators=[
            UniqueValidator(Department.objects.all(), "Name should be unique.")
        ],
    )

    class Meta:
        model = Department
        fields = ["id", "name", "budget"]
        read_only_fields = ["id", "pk"]

    def create(self, validated_data):
        return Department.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance
