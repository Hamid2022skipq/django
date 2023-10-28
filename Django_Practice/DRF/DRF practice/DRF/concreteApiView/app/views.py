from .models import Student
from .serializers import StudentSerailizers
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView

# class StudentList(ListAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerailizers

# class StudentRetrieve(RetrieveAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerailizers

# class StudentCreate(CreateAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerailizers

# class StudentUpdate(UpdateAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerailizers

# class StudentDestroy(DestroyAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerailizers

class StudentListCreate(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerailizers

# class StudentRetrieveDestroy(RetrieveDestroyAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerailizers

# class StudentRetrieveUpdate(RetrieveUpdateAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerailizers

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerailizers