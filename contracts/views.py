from django.shortcuts import render
from rest_framework.views import APIView, Response, status
from django.shortcuts import get_object_or_404
from .permissions import IsManager
from .models import Contract
from .serializers import ContractSerializer


class ContractView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManager]

    def get(self, request):
        contract = Contract.objects.all()
        serializer = ContractSerializer(contract, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        contract = ContractSerializer(data=request.data)
        contract.is_valid(raise_exception=True)
        contract.save(user=request.user)

        return Response(contract.data, status.HTTP_201_CREATED)


class ContractDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManager]

    def get(self, request, contract_id):
        contract = get_object_or_404(Contract, id=contract_id)
        serializer = ContractSerializer(contract)
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, contract_id):
        contract = get_object_or_404(Contract, id=contract_id)
        contract.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
