from django.db import models
from django.contrib.auth.models import AbstractUser


class Supplier(models.Model):
    name = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=20, unique=True)
    tel = models.CharField(max_length=20, unique=True)
    cnpj = models.CharField(max_length=15)


    category = models.ForeignKey(
            "categories.Category",
            on_delete=models.CASCADE,
            related_name="suppliers",
        )

    department = models.ForeignKey(
        "departments.Department",
        on_delete=models.CASCADE,
        related_name="suppliers",
    )