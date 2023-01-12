from rest_framework.test import APITestCase
from suppliers.models import Supplier
from employees.models import Employee


class SuppliersViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls):

        cls.employees = [
            Employee.objects.create_user(
                name=f"Employee {employee_id}",
                username=f"cleitinhu {employee_id}",
                email=f"managermiaw{employee_id}@mail.com ",
                password="1234",
                is_superuser=True,
            )
            for employee_id in range(1, 2)
        ]

        cls.BASE_URL = "/api/suppliers/"

        cls.suppliers = [
            Supplier.objects.create(
                name=f"Supplier {supplier_id}",
                email=f"supplier{supplier_id}@mail.com ",
                tel=f"4199156167{supplier_id}",
                cnpj=f"0277789069112{supplier_id}",
            )
            for supplier_id in range(1, 6)
        ]

    def test_create_new_supplier_with_manager_token(self):
        token = self.client.post(
            "/api/employees/login/",
            {"username": "cleitinhu 1", "password": "1234"},
            format="json",
        ).json()["access"]

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)
        response = self.client.post(
            self.BASE_URL,
            {
                "name": "Supplier9",
                "email": "supplier9@mail.com",
                "tel": "41991561679",
                "cnpj": "02777890691129",
            },
        )
        expected_status_code = 201

        self.assertEqual(expected_status_code, response.status_code)

        resulted_keys = response.json().keys()
        expected_keys = ["id", "name", "email", "tel", "cnpj"]
        message = "Check that all required keys are returned"

        for key in expected_keys:
            self.assertIn(key, resulted_keys, message)

    def test_can_list_all_suppliers(self):
        token = self.client.post(
            "/api/employees/login/",
            {"username": "cleitinhu 1", "password": "1234"},
            format="json",
        ).json()["access"]

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)
        response = self.client.get(self.BASE_URL)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(self.suppliers), len(response.data))

    def test_can_list_a_specific_supplier(self):
        token = self.client.post(
            "/api/employees/login/",
            {"username": "cleitinhu 1", "password": "1234"},
            format="json",
        ).json()["access"]

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)
        supplier = self.suppliers[0]
        response = self.client.get(f"{self.BASE_URL}{supplier.id}/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["id"], supplier.id)
