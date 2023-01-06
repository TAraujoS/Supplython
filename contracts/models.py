from django.db import models


class Contract(models.Model):
    duration = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.IntegerField(max_length=100)
    supplier = models.IntegerField(max_length=100)
