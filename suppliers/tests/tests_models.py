from django.test import TestCase
from suppliers.models import Supplier


class SupplierModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.supplier_data = {
            "name": "Casa dos Papeis",
            "email": "papeis@mail.com",
            "tel": "41991561673",
            "cnpj": "02777890691123",
        }

        cls.supplier = Supplier.objects.create(**cls.supplier_data)

    def test_name_max_length(self):
        max_length = self.supplier._meta.get_field("name").max_length

        self.assertEqual(max_length, 50)

    def test_name_is_unique(self):
        isUnique = self.supplier._meta.get_field("name").unique

        self.assertTrue(isUnique)

    def test_email_is_unique(self):
        isUnique = self.supplier._meta.get_field("email").unique

        self.assertTrue(isUnique)

    def test_cnpj_is_unique(self):
        isUnique = self.supplier._meta.get_field("cnpj").unique

        self.assertTrue(isUnique)

    def test_supplier_fields(self):
        self.assertEqual(self.supplier.name, self.supplier_data["name"])
        self.assertEqual(self.supplier.email, self.supplier_data["email"])
        self.assertEqual(self.supplier.tel, self.supplier_data["tel"])
        self.assertEqual(self.supplier.cnpj, self.supplier_data["cnpj"])
