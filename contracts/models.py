from django.db import models


class Contract(models.Model):
    duration = models.IntegerField(null=True, default=None)
    value = models.DecimalField(max=10)
