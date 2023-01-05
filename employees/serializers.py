from rest_framework import serializers
from .models import Employee
from rest_framework.validators import UniqueValidator
from departments.models import Department
from departments.serializer import DepartmentSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[
            UniqueValidator(Employee.objects.all(), "This field must be unique.")
        ]
    )

    is_manager = serializers.BooleanField(source="is_superuser")
    department_id = serializers.IntegerField()

    class Meta:
        model = Employee
        fields = [
            "id",
            "name",
            "username",
            "email",
            "password",
            "is_active",
            "is_manager",
            "department_id",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data: dict) -> Employee:

        if validated_data["is_superuser"]:
            employee = Employee.objects.create_superuser(**validated_data)
            return employee

        employee = Employee.objects.create_user(**validated_data)

        return employee


class DetailEmployeeSerializer(serializers.ModelSerializer):
    is_manager = serializers.BooleanField(source="is_superuser")
    department_id = serializers.IntegerField()
    department = DepartmentSerializer(read_only=True)

    class Meta:
        model = Employee
        fields = [
            "id",
            "name",
            "username",
            "email",
            "password",
            "is_active",
            "is_manager",
            "department_id",
            "department",
        ]

        extra_kwargs = {
            "password": {"write_only": True},
            "department_id": {"write_only": True},
        }

        read_only_fields = [
            "id",
            "department",
        ]

    def update(self, instance: Employee, validated_data: dict) -> Employee:

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.department = Department.objects.get(
            pk=validated_data.pop("department_id")
        )
        instance.save()

        return instance

    def get_fields(self, *args, **kwargs):

        fields = super().get_fields(*args, **kwargs)
        print(fields)
        request = self.context.get("request", None)
        if request and getattr(request, "method", None) == "POST":
            fields["department_id"].required = False

        return fields
