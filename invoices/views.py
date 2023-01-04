from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
from .serializers import InvoiceSerializer
from .models import Invoice


class InvoiceView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = []

    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()


class InvoiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = []

    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
