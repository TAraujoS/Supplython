from django.shortcuts import render
from .models import Supplier
from .serializers import SupplierSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..employees.permissions import IsManager


class SupplierView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManager]

    serializer_class = SupplierSerializer


class SupplierDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManager]

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
