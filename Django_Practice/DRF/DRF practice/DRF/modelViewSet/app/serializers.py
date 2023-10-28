from rest_framework import serializers
from .models import Student
class StudentSerailizers(serializers.ModelSerializer):
    class Meta:
       model=Student
       fields=['id','name','city','roll'] #'__all__'