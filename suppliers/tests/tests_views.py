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
            Supplier.objects.create_user(
                name=f"Supplier {supplier_id}",
                email=f"papeis{supplier_id}@mail.com ",
                tel="41991561673",
                cnpj="02777890691123",
            )
            for supplier_id in range(1, 6)
        ]

    def test_can_list_all_suppliers(self):
        response = self.client.get(self.BASE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(self.suppliers), len(response.data))

        for supplier in self.suppliers:
            self.assertIn(SupplierSerializer(instance=supplier).data, response.data)

    def test_can_list_a_specific_supplier(self):
        supplier = self.suppliers[0]
        response = self.client.get(f"{self.BASE_URL}{supplier.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["id"], supplier.id)

        self.assertEqual(SupplierSerializer(instance=supplier).data, response.data)

   