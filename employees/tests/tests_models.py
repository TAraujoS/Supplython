from django.test import TestCase
from employees.models import Employee
from departments.models import Department
from model_bakery import baker


class EmployeeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.employee_data = {
            "name": "ManagerMiaw",
            "username": "Miaw",
            "email": "managermiaw@mail.com",
            "password": "1234",
            "is_superuser": True,
        }

        cls.employee = Employee.objects.create(**cls.employee_data)

    def test_username_max_length(self):
        max_length = self.employee._meta.get_field("username").max_length

        self.assertEqual(max_length, 50)

    def test_username_is_unique(self):
        isUnique = self.employee._meta.get_field("username").unique

        self.assertTrue(isUnique)

    def test_password_max_length(self):
        max_length = self.employee._meta.get_field("password").max_length

        self.assertEqual(max_length, 100)

    def test_employee_fields(self):
        self.assertEqual(self.employee.name, self.employee_data["name"])
        self.assertEqual(self.employee.username, self.employee_data["username"])
        self.assertEqual(self.employee.email, self.employee_data["email"])
        self.assertEqual(self.employee.password, self.employee_data["password"])


# class EmployeeModelTestRelation(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.employees = [Employee.objects.create(cache=500000) for _ in range(20)]

#         cls.department = Department.objects.create(name="Health")

#     def test_department_may_contain_multiple_employees(self):

#         for employee in self.employees:
#             employee.department = self.department  # (4)
#             employee.save()

#         self.assertEquals(len(self.employees), self.department.employees.count())  # (5)

#         for employee in self.employees:
#             self.assertIs(employee.department, self.department)


# class EmployeeTestModel(TestCase):
#     @classmethod
#     def setUp(cls):
#         cls.employee = baker.make("employees.Employee")


# class DepartmentTestModel(TestCase):
#     @classmethod
#     def setUp(cls):
#         cls.department = baker.make("departments.Department")
