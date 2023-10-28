from django.contrib import admin
from django.urls import path
from curd.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/<int:pk>', serialization),
    path('stuinf/', studentinfo),
    path('stuCreate/', StudentCreate),
    path('stuUpdate/', StudentUpdate),
]
