from django.db import models


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=10)
    value = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=140)
    verified = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    validity = models.DateField()
