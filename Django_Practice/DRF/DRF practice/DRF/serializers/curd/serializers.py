from rest_framework import serializers
from .models import Student
class StudentSerializers(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    city=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()

    def create(self, validate_data):
        return Student.objects.create(**validate_data)
    def update(self,instance,validate_data):
        instance.name=validate_data.get('name',instance.name)
        instance.roll=validate_data.get('roll',instance.roll)
        instance.city=validate_data.get('city',instance.city)
        instance.save()
        return instance
        