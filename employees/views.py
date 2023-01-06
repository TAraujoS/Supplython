from .models import Employee
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import EmployeeSerializer, DetailEmployeeSerializer
from .permissions import IsManager, isAdminGet
from rest_framework import generics
from drf_spectacular.utils import extend_schema_view, extend_schema


@extend_schema_view(
    post=extend_schema(
        description="Route to create employees",
        summary="Create Employees",
        tags=["Employees"],
    ),
    get=extend_schema(
        description="Route for a superuser to list all employees",
        summary="List all employees",
        tags=["Employees"],
    ),
)
class EmployeeView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isAdminGet]

    queryset = Employee.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return DetailEmployeeSerializer

        return EmployeeSerializer


@extend_schema_view(
    get=extend_schema(
        description="Route for a superuser to list a single employee",
        summary="List employee",
        tags=["Employees"],
    ),
    patch=extend_schema(
        description="Route for a superuser to update an employee",
        summary="Update employee",
        tags=["Employees"],
    ),
)
class EmployeeDetailView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManager]

    queryset = Employee.objects.all()
    serializer_class = DetailEmployeeSerializer
