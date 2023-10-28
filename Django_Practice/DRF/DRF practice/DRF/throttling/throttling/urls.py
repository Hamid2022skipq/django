from django.contrib import admin
from django.urls import path, include
from app import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

# router object
router = DefaultRouter()

# registering router
router.register('studentapi', views.StudentModelViewSet1, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name='Obtainpairtoken'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='Refreshtoken'),
    path('verifytoken/',TokenVerifyView.as_view(),name='Verifytoken'),
]
