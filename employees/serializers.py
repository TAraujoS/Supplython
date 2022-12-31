from rest_framework import serializers
from .models import Employee
from rest_framework.validators import UniqueValidator


class EmployeeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[
            UniqueValidator(Employee.objects.all(), "This field must be unique.")
        ]
    )

    class Meta:
        model = Employee
        fields = [
            "id",
            "username",
            "email",
            "password",
            "is_manager",
            "is_superuser",
        ]
        read_only_fields = ["is_superuser"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict) -> Employee:

        if validated_data["is_manager"]:
            employee = Employee.objects.create_superuser(**validated_data)
            return employee

        employee = Employee.objects.create_user(**validated_data)

        return employee

    def update(self, instance: Employee, validated_data: dict) -> Employee:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
