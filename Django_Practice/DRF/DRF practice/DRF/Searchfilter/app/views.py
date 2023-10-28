from rest_framework.generics import ListAPIView
from .models import Student
from .serailizers import StudentSerializer
from rest_framework.filters import SearchFilter

class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends=[SearchFilter]

    # search by single fileds
    # search_fields=['city']

    # search by multiple column
    # search_fields=['city','name','roll','pass_by']

    # ^ represent the start with 
    search_fields=['city','^name','roll','pass_by']
