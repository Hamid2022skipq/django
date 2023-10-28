from rest_framework.generics import ListAPIView
from .models import Student
from .serailizers import StudentSerializer
from rest_framework.filters import SearchFilter,OrderingFilter

class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends=[SearchFilter,OrderingFilter]
    search_fields=['city','^name','roll','pass_by']
    # ordering_fields=['name']
    ordering_fields=['name','id','city']