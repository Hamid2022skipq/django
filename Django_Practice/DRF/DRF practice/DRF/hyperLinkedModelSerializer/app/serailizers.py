from .models import Student
from rest_framework import serializers

class StudentSerializer(serializers.HyperlinkedIdentityField):
    class Meta:
        model=Student
        fields=['id','urls','name','city','roll','pass_by']