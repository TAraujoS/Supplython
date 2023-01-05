from .models import Employee
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import EmployeeSerializer
from .permissions import IsManager, isAdminGet
from rest_framework import generics


class EmployeeView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isAdminGet]

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeDetailView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManager]

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# def perform_update(self, serializer):
#     instance = serializer.save()
#     send_email_confirmation(user=self.request.user, modified=instance)
