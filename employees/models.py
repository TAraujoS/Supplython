from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    email = models.EmailField(max_length=127, unique=True)
    is_manager = models.BooleanField(default=False)

    # department = models.ForeignKey(
    #     "suppliers.Department",
    #     on_delete=models.CASCADE,
    #     related_name="departments",
    # )

    def __repr__(self) -> str:
        return f"<[{self.id}] - {self.first_name}, {self.is_manager}>"
