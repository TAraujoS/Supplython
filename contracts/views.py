from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Contract
from .serializers import ContractSerializer
from ..employees.permissions import IsManager


class ContractView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classe = [IsManager]

    serializer_class = ContractSerializer
    queryset = Contract.objects.all()


class ContractDetailView(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classe = [IsManager]

    serializer_class = ContractSerializer
    queryset = Contract.objects.all()

    # lookup_url_kwarg = "contract_id"
