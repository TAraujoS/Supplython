from .models import Category
from .serializers import CategorySerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from employees.permissions import IsManager
from suppliers.models import Supplier
from django.shortcuts import get_object_or_404
import ipdb
from rest_framework.views import APIView, Response, Request, status


class CategoryView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManager]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        supplier = get_object_or_404(Supplier, id=self.request.data["supplier"])

        return serializer.save(supplier=supplier)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManager]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
