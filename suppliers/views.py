from django.shortcuts import render
from .models import Supplier
from .serializers import SupplierSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

<<<<<<< HEAD
# Create your views here.
=======
class SupplierView(generics.CreateAPIView):
    serializer_class = SupplierSerializer
    

class SupplierDetailView(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
>>>>>>> 2beb5cef052d7fc44b9135e82063b7af4f762159
