from django.contrib import admin
from django.urls import path, include
from app import views
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken.views import obtain_auth_token
from app.auths import CustomeAuth

# router object
router = DefaultRouter()

# registering router
router.register('studentapi', views.StudentModelViewSet1, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth',include('rest_framework.urls',namespace='rest_framework')),
    # path('gettoken/',obtain_auth_token )
    path('gettoken/',CustomeAuth.as_view())
]
