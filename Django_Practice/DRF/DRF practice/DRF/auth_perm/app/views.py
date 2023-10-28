from .models import Student
from .serializers import StudentSerailizers
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser

# Global authentication and permissions
# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerailizers


# Global authentication and local permissions
class StudentModelViewSet1(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerailizers
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAdminUser]

