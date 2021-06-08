from rest_framework import routers
from django.urls import path, include
from .views import UserLogin, UserRegistration

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("login/", UserLogin.as_view(), name='user-login'),
    path("register/", UserRegistration.as_view(), name='user-register'),
]
