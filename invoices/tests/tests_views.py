from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from .tests_invoices_factories import (
    create_manager,
    create_supplier,
    create_category,
    create_contract,
    update_supplier,
)
from rest_framework.views import status

client = APIClient()


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

    def test_invoice_creation_without_token(self):
        invoice_data = {
            "invoice_number": "58785",
            "value": "20000.00",
            "description": "Manutenção de Servidores Linux CentOS",
            "verified": False,
            "validity": "2023-02-10",
            "contract_id": 1,
            "employee_id": 1,
        }

        response = self.client.post(self.BASE_URL, data=invoice_data)

        # STATUS CODE
        expected_status_code = status.HTTP_401_UNAUTHORIZED
        resulted_status_code = response.status_code

        msg = (
            "Verifique se o status code retornado do POST sem token "
            + f"em `{self.BASE_URL}` é {expected_status_code}"
        )
        self.assertEqual(expected_status_code, resulted_status_code, msg)
