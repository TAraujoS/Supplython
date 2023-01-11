from django.test import TestCase
from .tests_invoices_factories import (
    create_manager,
    create_supplier,
    create_category,
    create_contract,
    update_supplier,
)
from invoices.models import Invoice
import ipdb


class InvoiceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        create_manager()
        create_supplier()
        create_category()
        create_contract()
        update_supplier()

        cls.invoice_data_1 = {
            "invoice_number": "58785",
            "value": "20000.00",
            "description": "Manutenção de Servidores Linux CentOS",
            "verified": False,
            "validity": "2023-02-10",
            "contract_id": 1,
            "employee_id": 1,
        }

        cls.invoice_1 = Invoice.objects.create(**cls.invoice_data_1)

    def test_invoice_number_1_max_length(self):
        invoice_number_max_length = self.invoice_1._meta.get_field(
            "invoice_number"
        ).max_length

        self.assertEqual(invoice_number_max_length, 10)

    def test_description_1_max_length(self):
        description_max_length = self.invoice_1._meta.get_field(
            "description"
        ).max_length

        self.assertEqual(description_max_length, 140)

    def test_invoices_fields(self):

        self.assertEqual(
            self.invoice_1.invoice_number, self.invoice_data_1["invoice_number"]
        )
        self.assertEqual(self.invoice_1.description, self.invoice_data_1["description"])
        self.assertEqual(self.invoice_1.value, self.invoice_data_1["value"])
        self.assertEqual(self.invoice_1.validity, self.invoice_data_1["validity"])
