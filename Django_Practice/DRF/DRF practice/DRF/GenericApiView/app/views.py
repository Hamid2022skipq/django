from django.shortcuts import render
from .models import Student
from .serializers import StudentSerailizers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

# Read all
class StudentList(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerailizers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    # Create

    serializer_class=StudentSerailizers
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

# Read Single
class StudentRetrieve(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerailizers
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    # Update

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    # Destroy

    serializer_class=StudentSerailizers
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
