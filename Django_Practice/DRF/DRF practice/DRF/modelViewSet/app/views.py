from .models import Student
from .serializers import StudentSerailizers
from rest_framework import viewsets

# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerailizers

class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerailizers
