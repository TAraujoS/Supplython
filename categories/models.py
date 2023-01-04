from django.db import models
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    # contract = models.ForeignKey(
    #     "contracts.Contract",
    #     on_delete=models.CASCADE,
    #     related_name="categories",
    # )
