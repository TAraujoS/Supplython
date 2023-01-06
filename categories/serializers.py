from rest_framework import serializers
from .models import Category
from suppliers.models import Supplier
from suppliers.serializers import SupplierSerializer
import ipdb

# from contracts.serializers import ContractSerializer


class CategorySerializer(serializers.ModelSerializer):
    # contract = ContractSerializer(read_only=True)
    # supplier = SupplierSerializer(read_only=True)
    supplier = serializers.IntegerField()

    class Meta:
        model = Category
        fields = ["id", "name", "supplier"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        # ipdb.set_trace()
        category = Category.objects.create(**validated_data)

        # supplier = get_object_or_404(Supplier, id=validated_data["supplier"])
        supplier = Supplier.objects.filter(id=validated_data["supplier"])

        # for supplier_dict in supplier:
        #     supplier_obj, created = Supplier.objects.get_or_create(**supplier_dict)
        category.supplier.add(supplier)

        category.save()

        return category
