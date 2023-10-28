from .models import Student
from .serializers import StudentSerailizers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Global authentication and local permissions
class StudentModelViewSet1(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerailizers
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]




# GEt Request
# http http://127.0.0.1:8000/studentapi/ 'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4MDAxNTA1LCJpYXQiOjE2OTc5OTg2NTUsImp0aSI6ImM4MjVkMjQzNzUzNjRjNDg5NWJlMTVmY2Q1NWVjZWE5IiwidXNlcl9pZCI6Mn0.xcl9NBmHrvCsz0dyIb4PvbzMEko18H_uYqbuURSjsvw'

# POST Request
# http PUT http://127.0.0.1:8000/studentapi/4 name=Rizwan roll=4 city=Narowal 'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4MDAyMTUwLCJpYXQiOjE2OTc5OTg2NTUsImp0aSI6IjJmM2FjZjNmNjk1ZTQ0MDJiZjVmZmY4NzRkMDk5ODA2IiwidXNlcl9pZCI6Mn0.fqHp5v1QdgbqZoBPrMhioW8kKDuZCsBVSpvEYqIu0iU'

# PUT Request
# http PUT http://127.0.0.1:8000/studentapi/4/ name=Rizwan roll=4 city=Narowal 'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4MDAyMjg5LCJpYXQiOjE2OTc5OTg2NTUsImp0aSI6ImMyNmYwZmQwZjVjYjQzNWE4NjBlYzMxN2YyM2RiZmQ4IiwidXNlcl9pZCI6Mn0.HfaMUzCJlzmTtvQTzaYxUtWpIK0qBz2XoS4_1yAm11k'



# Create a jwt toekn
# http POST http://127.0.0.1:8000/gettoken/ username='normal' password='django123'


# Verify token
# http POST http://127.0.0.1:8000/verifytoken/ token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk3OTk4OTU1LCJpYXQiOjE2OTc5OTg2NTUsImp0aSI6ImM5ZDJhZWY2Yzg4NzQ0MTI5OTY5ZGRlZGM3OWRkZDRkIiwidXNlcl9pZCI6Mn0.DbAHst5LDPXRSsmUZNfWhCGtKXSNyxLL6aavH2DRYXs"


# Create new access token from refresh token after previews access token expire 
# http POST http://127.0.0.1:8000/refreshtoken/ token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5ODA4NTA1NSwiaWF0IjoxNjk3OTk4NjU1LCJqdGkiOiI1OWVkMmZmZjNiMTc0ZmMyYmEwYzI4ZWFkZWIwZjAxNCIsInVzZXJfaWQiOjJ9.-xLENQ404zY5CuR6d8v90OVZVDKSOklUQBx-mskqBU4"


