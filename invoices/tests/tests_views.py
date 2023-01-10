# from rest_framework.test import APIClient
# from rest_framework.test import APITestCase
# from employees.models import Employee
# from employees.serializers import EmployeeSerializer

# client = APIClient()

# response_post = client.post(
#     "/api/employees/",
#     {
#         "name": "Manager",
#         "username": "manager10",
#         "email": "manager10@mail.com",
#         "password": "1234",
#         "is_manager": True,
#     },
#     format="json",
# )

# response_get = client.get("/api/employees/")

# response_get = client.get("/api/employees/1/")

# response_get = client.patch("/api/employees/1/", {"name": "Manager Juninho"})


# class EmployeesViewsTest(APITestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.employees = [
#             Employee.objects.create_user(
#                 name=f"Employee {employee_id}",
#                 username=f"cleitinhu {employee_id}",
#                 email=f"managermiaw{employee_id}@mail.com ",
#                 password="1234",
#                 is_superuser=True,
#             )
#             for employee_id in range(1, 6)
#         ]

#     def test_can_list_all_employees(self):
#         response = self.client.get("/api/employees/")
#         self.assertEqual(response.status_code, 200)

#         self.assertEqual(len(self.employees), len(response.data))

#         for employee in self.employees:
#             self.assertIn(EmployeeSerializer(instance=employee).data, response.data)

#     def test_can_retrieve_a_specific_employee(self):
#         employee = self.employees[0]
#         response = self.client.get(f"/api/employees/{employee.id}/")
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json()["id"], employee.id)

#         self.assertEqual(EmployeeSerializer(instance=employee).data, response.data)
