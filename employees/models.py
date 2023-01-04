from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    name = models.CharField(max_length=50, default="")
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    is_manager = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # department = models.ForeignKey(
    #     "suppliers.Department",
    #     on_delete=models.CASCADE,
    #     related_name="departments",
    # )

    def __repr__(self) -> str:
        return f"<[{self.id}] - {self.first_name}, {self.is_manager}>"
