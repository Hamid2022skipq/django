from .models import Student
from .serializers import StudentSerailizers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# To Create token from the ddrf cli use this command
# python3 manage.py drf_create_token user

# Global authentication and local permissions
class StudentModelViewSet1(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerailizers
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]


# Get Request for UnAuthenticated user
# http http://127.0.0.1:8000/studentapi/


# Get for Authenticated user
# http http://127.0.0.1:8000/studentapi/ 'Authorization:Token e1e4b9cc295b9353d94dfce00cce030f742aae15'

# POST for Authenticated user
# http -f POST http://127.0.0.1:8000/studentapi/ name=Rizwan roll=5 city=Narowal 'Authorization:Token e1e4b9cc295b9353d94dfce00cce030f742aae15'


# Put for Authenticated user
# http PUT http://127.0.0.1:8000/studentapi/5/ name=Rizwan roll=5 city=Suadia_Arabia 'Authorization:Token e1e4b9cc295b9353d94dfce00cce030f742aae15'


# DELETE for Authenticated user
# http DELETE http://127.0.0.1:8000/studentapi/5/ 'Authorization:Token e1e4b9cc295b9353d94dfce00cce030f742aae15'

