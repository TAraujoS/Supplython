from rest_framework import generics
from .serializer import DepartmentSerializer
from .models import Department
from rest_framework_simplejwt.authentication import JWTAuthentication
from employees.permissions import IsManager


class DepartmentView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManager]

    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManager]

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
