from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from suppliers.models import Supplier
from suppliers.serializers import SupplierSerializer


client = APIClient()

response_post = client.post(
    "/api/suppliers/",
    {
        "name": "Casa dos Papeis",
        "email": "papeis@mail.com",
        "tel": "41991561673",
        "cnpj": "02777890691123"
    },
    format="json",
)


class SuppliersViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.BASE_URL = "/api/suppliers/"


        cls.suppliers = [
            Supplier.objects.create(
                name=f"Supplier {supplier_id}",
                email=f"papeis{supplier_id}@mail.com ",
                tel=f"4199156167{supplier_id}",
                cnpj=f"0277789069112{supplier_id}",
            )
            for supplier_id in range(1, 6)
        ]

    def test_can_list_all_suppliers(self):
        response = self.client.get(self.BASE_URL)
        expected_status_code = 200

        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(len(self.suppliers), len(response.data))

        for supplier in self.suppliers:
            self.assertIn(SupplierSerializer(instance=supplier).data, response.data)

    def test_can_list_a_specific_supplier(self):
        supplier = self.suppliers[0]
        response = self.client.get(f"{self.BASE_URL}{supplier.id}/")
        expected_status_code = 200

        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(response.json()["id"], supplier.id)

        self.assertEqual(SupplierSerializer(instance=supplier).data, response.data)

    def test_create_a_new_supplier(self):
        response = self.client.post(self.BASE_URL, response_post)
        expected_status_code = 201

        self.assertEqual(expected_status_code, response.status_code)

        resulted_keys = response.json().keys()
        expected_keys = ['id', 'name', 'email', 'tel', 'cnpj', 'contracts', 'departments']
        message = 'Verifique se todas as chaves obrigatórias são retornadas'

        for key in expected_keys:
            self.assertIn(key, resulted_keys, message)

    