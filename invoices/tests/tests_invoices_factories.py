from employees.models import Employee
from suppliers.models import Supplier
from categories.models import Category
from contracts.models import Contract
from rest_framework_simplejwt.tokens import RefreshToken

import ipdb


class SuplementsCreator:
    def create_manager() -> tuple[Employee, RefreshToken]:
        manager_data = {
            "name": "Rochelle",
            "username": "rochelle",
            "email": "rochelle@mail.com",
            "password": "1234",
            "is_superuser": True,
        }

        manager = Employee.objects.create_superuser(**manager_data)
        manager_token = RefreshToken.for_user(manager)

        return manager, manager_token

    def create_employee() -> tuple[Employee, RefreshToken]:
        employee_data = {
            "name": "Julius",
            "username": "julius",
            "email": "lowprice@mail.com",
            "password": "4321",
            "is_superuser": False,
        }

        employee = Employee.objects.create_user(**employee_data)
        employee_token = RefreshToken.for_user(employee)

        return employee, employee_token

    def create_supplier() -> tuple[Contract]:
        supplier_data_1 = {
            "name": "RTI Soluctions",
            "email": "rti.soluctions@mail.com",
            "tel": "4135233561",
            "cnpj": "27335286000101",
        }

        supplier_data_2 = {
            "name": "Martins Informática",
            "email": "martins.informatica@mail.com",
            "tel": "413522245",
            "cnpj": "04587873000101",
        }

        supplier_1 = Supplier.objects.create(**supplier_data_1)
        suplier_2 = Supplier.objects.create(**supplier_data_2)

        return supplier_1, suplier_2

    def create_category() -> tuple[Category]:
        category_data_1 = {"name": "Manutenção de Servidores", "supplier": 1}
        category_data_2 = {"name": "Departamento de T.I.", "supplier": 2}

        category_1 = Category.objects.create(**category_data_1)
        category_2 = Category.objects.create(**category_data_2)

        return category_1, category_2

    def create_contract() -> tuple[Contract]:
        contract_data_1 = {
            "duration": "2025-01-01",
            "value": "500000.00",
            "category_id": 1,
            "supplier_id": 1,
        }

        contract_data_2 = {
            "duration": "2025-05-07",
            "value": "800000.00",
            "category_id": 2,
            "supplier_id": 2,
        }

        contract_1 = Contract.objects.create(**contract_data_1)
        contract_2 = Contract.objects.create(**contract_data_2)

        return contract_1, contract_2
