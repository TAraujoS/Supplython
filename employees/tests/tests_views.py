from rest_framework.test import APITestCase
from employees.models import Employee


class EmployeesViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls):

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
            for employee_id in range(1, 2)
        ]

    def test_create_common_user(self):
        url = "/api/employees/"

        response = self.client.post(url, self.employeeNotAdmin)
        expected_status_code = 201
        message = "verify if status code 201 is returning"

        self.assertEqual(expected_status_code, response.status_code, message)

        resulted_keys = response.json().keys()
        expected_keys = ["id", "name", "username", "email", "is_manager"]
        message = "verify is all keys are being returned"
        for key in expected_keys:
            self.assertIn(key, resulted_keys, message)

    def test_can_list_all_employees(self):
        token = self.client.post(
            "/api/employees/login/",
            {"username": "cleitinhu 1", "password": "1234"},
            format="json",
        ).json()["access"]

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)
        response = self.client.get("/api/employees/")
        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(self.employees), len(response.data))
        list = [
            {
                "username": self.employees[0].username,
                "id": self.employees[0].id,
                "name": self.employees[0].name,
            }
        ]
        # for employee in self.employees:
        # self.assertIn(list, response.data)

    def test_can_retrieve_a_specific_employee(self):
        token = self.client.post(
            "/api/employees/login/",
            {"username": "cleitinhu 1", "password": "1234"},
            format="json",
        ).json()["access"]

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)
        employee = self.employees[0]
        response = self.client.get(f"/api/employees/{employee.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["id"], employee.id)

        # self.assertEqual(EmployeeSerializer(instance=employee).data, response.data)
