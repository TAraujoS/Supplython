from django.db import models


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=10)
    value = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=140)
    verified = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    validity = models.DateField()

    contract = models.ForeignKey(
        "contracts.Contract",
        on_delete=models.CASCADE,
        related_name="invoices",
    )

    employee = models.ForeignKey(
        "employees.Employee",
        on_delete=models.CASCADE,
        related_name="invoices",
    )

    def __repr__(self) -> str:
        return f"<[{self.id}] - {self.invoice_number}, {self.description}, {self.validity}, {self.description}>"
    