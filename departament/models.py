from django.db import models


class Departament(models.Model):
    name = models.CharField(max_length=50)
    budget = models.DecimalField(max_digits=10, decimal_places=2 )



