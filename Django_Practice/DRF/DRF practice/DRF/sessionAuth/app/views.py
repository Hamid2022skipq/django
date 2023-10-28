from .models import Student
from .serializers import StudentSerailizers
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly

# Global authentication and local permissions
class StudentModelViewSet1(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerailizers
    authentication_classes=[SessionAuthentication]
    # permission_classes=[IsAuthenticated]
    # permission_classes=[AllowAny]
    # permission_classes=[IsAdminUser] 
    # permission_classes=[IsAuthenticatedOrReadOnly] 

    # we need to provide change permissions from the admin panel for post request 
    # permission_classes=[DjangoModelPermissions] 

    # unautherticated user has only readonly feature to api
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly] 

