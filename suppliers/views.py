from .models import Supplier
from .serializers import SupplierSerializer, SupplierDetailSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from employees.permissions import IsManager


class SupplierView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManager]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return SupplierDetailSerializer

        return SupplierSerializer

    queryset = Supplier.objects.all()

    
class SupplierDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManager]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return SupplierDetailSerializer

        return SupplierSerializer

    queryset = Supplier.objects.all()
