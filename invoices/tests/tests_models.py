from django.test import TestCase
from .tests_invoices_factories import (
    create_manager,
    create_supplier,
    create_category,
    create_contract,
)
from invoices.models import Invoice


class InvoiceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        create_manager()
        create_supplier()
        create_category()
        create_contract()

        invoice_data_1 = {
            "invoice_number": "58785",
            "value": "20000.00",
            "description": "Manutenção de Servidores Linux CentOS",
            "verified": False,
            "validity": "2023-02-10",
            "supplier_id": 1,
            "contract_id": 1,
            "employee_id": 1,
        }

        invoice_data_2 = {
            "invoice_number": "58786",
            "value": "4430.00",
            "description": "5 Toners HP5898, 10 resmas chamequinho, 5 mouses RGB, 5 teclados soft logitec",
            "verified": False,
            "validity": "2023-05-10",
            "supplier_id": 2,
            "contract_id": 2,
            "employee_id": 1,
        }

        cls.invoice_1 = Invoice.objects.create(**invoice_data_1)
        cls.invoice_2 = Invoice.objects.create(**invoice_data_2)

    def test_invoice_number_1_max_length(self):
        invoice_number_max_length = self.invoice_1._meta.get_field(
            "invoice_number"
        ).max_length

        self.assertEqual(invoice_number_max_length, 10)

    def test_invoice_number_2_max_length(self):
        invoice_number_max_length = self.invoice_2._meta.get_field(
            "invoice_number"
        ).max_length

        self.assertEqual(invoice_number_max_length, 10)

    def test_description_1_max_length(self):
        description_max_length = self.invoice_1._meta.get_field(
            "description"
        ).max_length

        self.assertEqual(description_max_length, 140)

    def test_description_2_max_length(self):
        description_max_length = self.invoice_2._meta.get_field(
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

        self.assertEqual(
            self.invoice_2.invoice_number, self.invoice_data_2["invoice_number"]
        )
        self.assertEqual(self.invoice_2.description, self.invoice_data_2["description"])
        self.assertEqual(self.invoice_2.value, self.invoice_data_2["value"])
        self.assertEqual(self.invoice_2.validity, self.invoice_data_2["validity"])
