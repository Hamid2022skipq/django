# from rest_framework.pagination import PageNumberPagination

# class MyPageNumberPagination(PageNumberPagination):
#     page_size=6
#     page_query_param='p'
#     page_size_query_param='records'
#     max_page_size=7
#     last_page_strings='end'


# from rest_framework.pagination import LimitOffsetPagination
# class MyLimitOffsetPagination(LimitOffsetPagination):
#     pass
#     limit_query_param='L'
#     offset_query_param='O'
#     default_limit=5
#     max_limit=7
    
from rest_framework.pagination import CursorPagination
class MyCursorPagination(CursorPagination):
    page_size=5
    ordering='name'
    cursor_query_param='cu'
    max_page_size=7