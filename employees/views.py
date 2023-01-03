from .models import Employee
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import EmployeeSerializer
from .permissions import isAdmin
from rest_framework import generics


class EmployeeView(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isAdmin]

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
