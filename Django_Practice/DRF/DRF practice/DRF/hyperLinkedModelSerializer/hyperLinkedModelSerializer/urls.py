from django.contrib import admin
from django.urls import path, include
from app import views
from rest_framework.routers import DefaultRouter
# router object
router = DefaultRouter()

# registering router
router.register('studentapi', views.StudentListAPIView, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
