from rest_framework.test import APITestCase
from .tests_invoices_factories import (
    create_manager,
    create_supplier,
    create_category,
    create_contract,
    update_supplier,
)


class InvoicesViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls):

        cls.BASE_URL = "/api/invoices/"
        cls.BASE_DETAIL_URL = cls.BASE_URL + "1/"
        cls.maxDiff = None

        cls.manager, cls.token = create_manager()
        cls.supplier = create_supplier()
        cls.category = create_category()
        cls.contract = create_contract()
        cls.update_supplier = update_supplier()

    def test_invoice_creation_with_token(self):

        invoice_data = {
            "invoice_number": "587982",
            "value": "20000.00",
            "description": "Manutenção de Servidores Linux CentOS",
            "verified": False,
            "validity": "2023-02-10",
            "contract_id": 1,
            "employee_id": 1,
        }

        token = self.client.post(
            "/api/employees/login/",
            {"username": "rochelle", "password": "1234"},
            format="json",
        ).json()["access"]

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)

        response = self.client.post(
            self.BASE_URL,
            invoice_data,
        )

        expected_status_code = 201

        msg = (
            "Check if the status code returned from the POST"
            + f"em `{self.BASE_URL}` é {expected_status_code}"
        )
        self.assertEqual(expected_status_code, response.status_code, msg)

    def test_invoice_repeated_creation_(self):
        url = "/api/invoices/"

        invoice_data = {
            "invoice_number": "587982",
            "value": "20000.00",
            "description": "Manutenção de Servidores Linux CentOS",
            "verified": False,
            "validity": "2023-02-10",
            "contract_id": 1,
            "employee_id": 1,
        }

        token = self.client.post(
            "/api/employees/login/",
            {"username": "rochelle", "password": "1234"},
            format="json",
        ).json()["access"]

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)

        response = self.client.post(
            self.BASE_URL,
            invoice_data,
        )

        expected_status_code = 201

        msg = (
            "Check if the status code returned from the POST"
            + f"em `{self.BASE_URL}` é {expected_status_code}"
        )
        self.assertEqual(expected_status_code, response.status_code, msg)

    def test_invoice_creation_with_invalid_fields(self):

        invoice_data = {
            "value": "20000.00",
            "description": "Manutenção de Servidores Linux CentOS",
            "verified": False,
            "validity": "2023-02-10",
            "contract_id": 1,
            "employee_id": 1,
        }

        token = self.client.post(
            "/api/employees/login/",
            {"username": "rochelle", "password": "1234"},
            format="json",
        ).json()["access"]

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)

        response = self.client.post(
            self.BASE_URL,
            invoice_data,
        )

        expected_status_code = 400

        msg = (
            "Check if the status code returned from the POST"
            + f"em `{self.BASE_URL}` é {expected_status_code}"
        )
        self.assertEqual(expected_status_code, response.status_code, msg)

    def test_invoice_creation_with_invalid_date(self):

        invoice_data = {
            "invoice_number": "587982",
            "value": "20000.00",
            "description": "Manutenção de Servidores Linux CentOS",
            "verified": False,
            "validity": "10-02-24",
            "contract_id": 1,
            "employee_id": 1,
        }

        token = self.client.post(
            "/api/employees/login/",
            {"username": "rochelle", "password": "1234"},
            format="json",
        ).json()["access"]

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)

        response = self.client.post(
            self.BASE_URL,
            invoice_data,
        )

        expected_status_code = 400

        msg = (
            "Check if the status code returned from the POST"
            + f"em `{self.BASE_URL}` é {expected_status_code}"
        )
        self.assertEqual(expected_status_code, response.status_code, msg)

    def test_get_invoice_list_(self):
        token = self.client.post(
            "/api/employees/login/",
            {"username": "rochelle", "password": "1234"},
            format="json",
        ).json()["access"]

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)

        response = self.client.get(self.BASE_URL)

        expected_status_code = 200

        msg = (
            "Check if the status code returned from the GET"
            + f"in `{self.BASE_URL}` is {expected_status_code}"
        )
        self.assertEqual(expected_status_code, response.status_code, msg)
