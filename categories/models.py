from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    supplier = models.ManyToManyField(
        "suppliers.Supplier",
        related_name="categories",
    )

    def __repr__(self) -> str:
        return f"<[{self.id}] - {self.name}>"
