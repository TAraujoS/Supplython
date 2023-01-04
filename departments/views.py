from rest_framework import generics
from .serializer import DepartmentSerializer
from .models import Department


class DepartmentView(generics.ListCreateAPIView):

    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    lookup_url_kwarg = "pk"
