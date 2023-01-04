from rest_framework import serializers
from .models import Contract


class ContractSerializer(serializers.Serializer):
    class Meta:
        model = Contract
        fields = ["id", "duration", "value"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        return Contract.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance
<<<<<<< HEAD
=======
