from rest_framework.generics import ListAPIView
from .models import Student
from .serailizers import StudentSerializer
from rest_framework.filters import SearchFilter,OrderingFilter
# from .paginations import MyPageNumberPagination
# from .paginations import MyLimitOffsetPagination
from .paginations import MyCursorPagination

class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # filter_backends=[SearchFilter,OrderingFilter]
    # search_fields=['city','^name','roll','pass_by']
    # ordering_fields=['name','id','city']
    # pagination_class=MyPageNumberPagination
    # pagination_class=MyLimitOffsetPagination
    pagination_class=MyCursorPagination
