from django.test import TestCase
from employees.models import Employee
from departments.models import Department


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


class EmployeeModelTestRelation(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.employees = [
            Employee.objects.create_user(
                name="cleitu",
                username="cleitinhu",
                email="cleitinhu@mail.com",
                password="1234",
                is_superuser=True,
            ),
            Employee.objects.create_user(
                name="cleituS",
                username="cleitinhuS",
                email="cleitinhuS@mail.com",
                password="1234",
                is_superuser=True,
            ),
        ]

        cls.department = Department.objects.create(
            name="T.I",
            budget="500000.80",
        )

    def test_department_may_contain_multiple_employees(self):

        for employee in self.employees:
            employee.department = self.department
            employee.save()

        self.assertEquals(len(self.employees), self.department.employees.count())

        for employee in self.employees:
            self.assertIs(employee.department, self.department)
