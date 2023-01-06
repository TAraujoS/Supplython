from django.test import TestCase
from employees.models import Employee
from model_bakery import baker


class EmployeeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.employee_data = {
            "name": "ManagerMiaw",
            "username": "Miaw",
            "email": "managermiaw@mail.com",
            "password": "1234",
            "is_manager": True,
        }

        cls.employee = Employee.objects.create(**cls.employee_data)

    def test_username_max_length(self):
        max_length = self.employee._meta.get_field("username").max_length

        self.assertEqual(max_length, 50)


# class EmployeeTestModel(TestCase):
#     @classmethod
#     def setUp(cls):
#         cls.employee = baker.make("employees.Employee")


# class DepartmentTestModel(TestCase):
#     @classmethod
#     def setUp(cls):
#         cls.department = baker.make("departments.Department")


# class YourTestClass(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         Employee.objects.create(
#             name="Cleitinho",
#             username="cleitin22",
#             email="cleitin22@mail.com",
#             password="1234",
#             is_manager=True,
#         )
#         Employee.objects.create(
#             name="Juninho",
#             username="junin22",
#             email="junin22@mail.com",
#             password="1234",
#             is_manager=False,
#         )

#     def setUp(self):
#         pass

#     def tearDown(self):
#         pass

#     def test_something_that_will_pass(self):
#         self.assertFalse(False)

#     def test_something_that_will_fail(self):
#         self.assertTrue(False)
