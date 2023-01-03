from rest_framework import serializers
from .models import Contract


class ContractSerializer(serializers.Serializer):

    id = id = serializers.CharField(read_only=True)
    duration = serializers.IntegerField(read_only=True)
    value = serializers.DecimalField(max=10)

    def create(self, validated_data):
        contract = Contract.objects.create(**validated_data)
        return contract


def validate_contract(self, contract):
    contract_already_exists = Contract.objects.filter(contract=contract).exists()

    if contract_already_exists:
        raise serializers.ValidationError(detail="contract already exists.")
    return contract
