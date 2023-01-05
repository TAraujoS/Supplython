from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    is_superuser = models.BooleanField(default=False, null=True)
    is_active = models.BooleanField(default=True)
    department = models.ForeignKey(
        "departments.Department",
        on_delete=models.CASCADE,
        related_name="employees",
        null=True,
    )

    def __repr__(self) -> str:
        return f"<[{self.id}] - {self.first_name}, {self.is_superuser}>"
