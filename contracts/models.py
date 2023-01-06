from django.db import models


class Contract(models.Model):
    duration = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=2)

    # N:1 -> category -> contract
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        related_name="contracts",
    )
    # N:1 ->  suppliers -> contract
    supplier = models.ForeignKey(
        "suppliers.Supplier",
        on_delete=models.CASCADE,
        related_name="contracts",
    )
