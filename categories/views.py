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

    def post(self, req: Request) -> Response:
        serializer = CategorySerializer(data=req.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManager]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
