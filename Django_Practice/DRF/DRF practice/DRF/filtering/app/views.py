from rest_framework.generics import ListAPIView
from .models import Student
from .serailizers import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend

class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    # queryset = Student.objects.filter(pass_by='normal')
    serializer_class = StudentSerializer

    # this show what user entered in bd just and not what other enter 
    # def get_queryset(self):
    #     user=self.request.user
    #     return Student.objects.filter(pass_by=user)

    # This is per view


    # http://127.0.0.1:8000/api/?city=Narowal get
    filter_backends=[DjangoFilterBackend]
    # filterset_fields=['city']
    filterset_fields=['city','name']
