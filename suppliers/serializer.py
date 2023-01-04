from rest_framework import serializers


from .models import Departament

class DepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departament
        fields = "__all__"
        read_only_fields = ["pk"]

    def create(self,validated_data):
        return Departament.objects.create(**validated_data)
    
    def update(self,instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance