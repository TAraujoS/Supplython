from rest_framework import serializers
from .models import Contract


class ContractSerializer(serializers.Serializer):
    class Meta:
        model = Contract
        fields = ["id", "duration", "budget"]

    def create(self, validated_data):
        return Contract.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance


# def validate_contract(self, contract):
#     contract_already_exists = Contract.objects.filter(contract=contract).exists()

#     if contract_already_exists:
#         raise serializers.ValidationError(detail="contract already exists.")
#     return contract

