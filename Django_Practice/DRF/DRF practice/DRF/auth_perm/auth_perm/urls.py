from django.contrib import admin
from django.urls import path, include
from app import views
from rest_framework.routers import DefaultRouter

# router object
router = DefaultRouter()

# registering router
router.register('studentapi', views.StudentModelViewSet1, basename='student')
# router.register('studentapi', views.StudentReadOnlyModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
