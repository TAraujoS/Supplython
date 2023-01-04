
from rest_framework import generics
from .serializer import DepartamentSerializer
from .models import Departament

class DepartamentView(generics.ListCreateAPIView):

    serializer_class = DepartamentSerializer
    queryset = Departament.objects.all()


class DepartamentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Departament.objects.all()
    serializer_class = DepartamentSerializer
    
    lookup_url_kwarg = "pk"
