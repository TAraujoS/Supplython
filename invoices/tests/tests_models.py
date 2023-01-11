from django.test import TestCase
from .tests_invoices_factories import (
    create_manager,
    create_supplier,
    create_category,
    create_contract,
    update_supplier,
    create_invoice,
)


class InvoiceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        create_manager()
        create_supplier()
        create_category()
        create_contract()
        update_supplier()
        cls.invoice = create_invoice()

        cls.invoice_data = {
            "invoice_number": "58785",
            "value": "20000.00",
            "description": "Manutenção de Servidores Linux CentOS",
            "verified": False,
            "validity": "2023-02-10",
            "contract_id": 1,
            "employee_id": 1,
        }

    def test_invoice_number_max_length(self):
        invoice_number_max_length = self.invoice._meta.get_field(
            "invoice_number"
        ).max_length

        self.assertEqual(invoice_number_max_length, 10)

    def test_description_max_length(self):
        description_max_length = self.invoice._meta.get_field("description").max_length

        self.assertEqual(description_max_length, 140)

    def test_invoices_fields(self):

        self.assertEqual(
            self.invoice.invoice_number, self.invoice_data["invoice_number"]
        )
        self.assertEqual(self.invoice.description, self.invoice_data["description"])
        self.assertEqual(self.invoice.value, self.invoice_data["value"])
        self.assertEqual(self.invoice.validity, self.invoice_data["validity"])
