from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["name", "budget"]
        extra_kwargs = {
            "name": {
                "validators": [UniqueValidator(Department.objects.all())],
            }
        }
        read_only_fields = ["pk"]

    def create(self, validated_data):
        return Department.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance
