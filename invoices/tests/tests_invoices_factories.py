from employees.models import Employee
from suppliers.models import Supplier
from categories.models import Category
from contracts.models import Contract
from rest_framework_simplejwt.tokens import RefreshToken


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


def create_supplier() -> Supplier:
    supplier_data_1 = {
        "name": "RTI Soluctions",
        "email": "rti.soluctions@mail.com",
        "tel": "4135233561",
        "cnpj": "27335286000101",
    }

    supplier_1 = Supplier.objects.create(**supplier_data_1)

    return supplier_1


def create_category() -> Category:
    category_data_1 = {"name": "Manutenção de Servidores"}

    category_1 = Category.objects.create(**category_data_1)

    return category_1


def create_contract() -> Contract:
    contract_data_1 = {
        "duration": "2025-01-01",
        "value": "500000.00",
        "category_id": 1,
    }

    contract_1 = Contract.objects.create(**contract_data_1)

    return contract_1


def update_supplier() -> Supplier:

    supplier = Supplier.objects.get(id=1)

    setattr(supplier, "contract_id", 1)

    supplier.save()

    return supplier
