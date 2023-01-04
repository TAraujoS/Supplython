from django.db import models


class Contract(models.Model):
    duration = models.DateField(required=True)
    value = models.DecimalField(max=10)
