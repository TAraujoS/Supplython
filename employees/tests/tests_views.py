from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from employees.models import Employee
from employees.serializers import EmployeeSerializer
import ipdb

client = APIClient()

response_post = client.post(
    "/api/employees/",
    {
        "name": "Manager",
        "username": "manager10",
        "email": "manager10@mail.com",
        "password": "1234",
        "is_manager": True,
    },
    format="json",
)

response_get = client.get("/api/employees/")

response_get = client.get("/api/employees/1/")

response_get = client.patch("/api/employees/1/", {"name": "Manager Juninho"})


class EmployeesViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.employeeNotAdmin = {
            "name": "Cleitu",
            "username": "cleitinhuu",
            "email": "cleitinhu@mail.com ",
            "password": "1234",
            "is_superuser": False,
        }

        cls.employees = [
            Employee.objects.create_user(
                name=f"Employee {employee_id}",
                username=f"cleitinhu {employee_id}",
                email=f"managermiaw{employee_id}@mail.com ",
                password="1234",
                is_superuser=True,
            )
            for employee_id in range(1, 6)
        ]

        cls.manager = [
            Employee.objects.create_user(
                name=f"John",
                username=f"Johnas",
                email=f"john@mail.com ",
                password="1234",
                is_superuser=True,
            )
        ]

    def test_create_common_user(self):
        url = "/api/employees/"

        response = self.client.post(url, self.employeeNotAdmin, format="json")
        expected_status_code = 201
        message = "verify if status code 201 is returning"

        self.assertEqual(expected_status_code, response.status_code, message)

        resulted_keys = response.json().keys()
        expected_keys = ["id", "name", "username", "email", "password", "is_manager"]
        message = "verify is all keys are being returned"
        for key in expected_keys:
            self.assertIn(key, resulted_keys, message)

    # def test_can_list_all_employees(self):
    #     url = "/api/employees/"
    #     response = self.client.get(url, self.employees, format="json")
    #     self.assertEqual(response.status_code, response.status_code)
    #     ipdb.set_trace()
    #     self.assertEqual(len(self.employees), len(response.data))

    #     for employee in self.employees:
    #         self.assertIn(EmployeeSerializer(instance=employee).data, response.data)

    # def test_can_retrieve_a_specific_employee(self):

    #     employee = self.employees[0]
    #     response = self.client.get(f"/api/employees/{employee.id}/")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json()["id"], employee.id)

    #     self.assertEqual(EmployeeSerializer(instance=employee).data, response.data)
