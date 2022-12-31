from .models import Employee
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import EmployeeSerializer
from .permissions import isAdminOrAccountOwner
from rest_framework import generics


class EmployeeView(generics.CreateAPIView):
    serializer_class = EmployeeSerializer


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isAdminOrAccountOwner]

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
