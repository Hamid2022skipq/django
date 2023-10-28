from .models import Student
from .serializers import StudentSerailizers
from .customePermissions import MyPermission
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication


# Global authentication and local permissions
class StudentModelViewSet1(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerailizers
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermission]
