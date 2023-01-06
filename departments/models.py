from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=50)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ManyToManyField("suppliers.Supplier", related_name="departments")