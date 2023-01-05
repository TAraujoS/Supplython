from .models import Employee
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import EmployeeSerializer, DetailEmployeeSerializer
from .permissions import IsManager, isAdminGet
from rest_framework import generics


class EmployeeView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isAdminGet]

    queryset = Employee.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return DetailEmployeeSerializer

        return EmployeeSerializer


class EmployeeDetailView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManager]

    queryset = Employee.objects.all()
    serializer_class = DetailEmployeeSerializer
