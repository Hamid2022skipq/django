from rest_framework import viewsets
from .models import Student
from .serailizers import StudentSerializer

class StudentListAPIView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
