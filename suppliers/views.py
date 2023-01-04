from django.shortcuts import render
from .models import Supplier
from .serializers import SupplierSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class SupplierView(generics.CreateAPIView):
    serializer_class = SupplierSerializer


class SupplierDetailView(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
