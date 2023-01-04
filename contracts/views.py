from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsManager
from .models import Contract
from .serializers import ContractSerializer

    class ContractView(generics.ListCreateAPIView):
        serializer_class = ContractSerializer
        queryset = Contract.objects.all()

    #class ContractDetailView(generics.RetrieveUpdateDestroyAPIView):
        """
        APIView
        has_object_permission -> self.check_object_permission
"""

    #authentication_classes = [JWTAuthentication]
    # AND
    #permission_classe = [IsManager]

    #serializer_class = ContractSerializer
    #queryset = Contract.objects.all()

    #lookup_url_kwarg = "contract_id"
