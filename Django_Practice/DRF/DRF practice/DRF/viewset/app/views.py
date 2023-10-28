from .models import Student
from .serializers import StudentSerailizers
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response 

class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        stu=Student.objects.all()
        serializer=StudentSerailizers(stu,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk):
        if pk is not None:
            stu=Student.objects.get(id=pk)
            serializer=StudentSerailizers(stu)
            return Response(serializer.data)
    
    def create(self,request):
        serializer=StudentSerailizers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created (:'},status=status.HTTP_201_CREATED)
        return Response({'msg':'Error will Creating'},status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk):
        if pk is not None:
            stu=Student.objects.get(id=pk)
            serializer=StudentSerailizers(stu,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data Updated (:'},status=status.HTTP_201_CREATED)
        return Response({'msg':'Error will Updating'},status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):
        if pk is not None:
            stu=Student.objects.get(id=pk)
            serializer=StudentSerailizers(stu,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Partial Data Updated (:'},status=status.HTTP_201_CREATED)
        return Response({'msg':'Error will Updating'},status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk):
        if pk:
            stu=Student.objects.get(id=pk)
            stu.delete()
            return Response({'msg':'Data Deleted ):'},status=status.HTTP_201_CREATED)
        return Response({'msg':'Error will Deleting'},status=status.HTTP_400_BAD_REQUEST)
