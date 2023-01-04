from django.db import models


class Contract(models.Model):
    duration = models.DateField(required=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
