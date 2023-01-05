from django.db import models


class Contract(models.Model):
    duration = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.IntegerField(max_length=100)
    supplier = models.IntegerField(max_length=100)


    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        related_name="contracts",
    )

    supplier = models.ForeignKey(
        "suppliers.Supplier",
        on_delete=models.CASCADE,
        related_name="contracts",
    )