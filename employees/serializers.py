from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from employees.models import Employee
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

    def get_fields(self, *args, **kwargs):

        fields = super().get_fields(*args, **kwargs)
        request = self.context.get("request", None)
        if request and getattr(request, "method", None) == "POST":
            fields["department_id"].required = False

        return fields


class DetailEmployeeSerializer(serializers.ModelSerializer):
    is_manager = serializers.BooleanField(source="is_superuser")
    department_id = serializers.IntegerField(write_only=True)
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
        department_id = validated_data.pop("department_id", None)

        if department_id:
            instance.department = Department.objects.get(pk=department_id)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
