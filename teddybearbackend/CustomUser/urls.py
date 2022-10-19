
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from . import views

router = DefaultRouter()
router.register('login', views.LoginViewSet, 'login')
router.register('register', views.UserViewSet, 'register')


urlpatterns = [
    path('', include(router.urls)),
    # path('register/', views.RegistrationAPI.as_view(), name='register'),
]
