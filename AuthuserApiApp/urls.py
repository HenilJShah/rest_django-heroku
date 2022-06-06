from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import StudentAuthApi

router = DefaultRouter()

router.register('auth', StudentAuthApi, basename='api')

urlpatterns = router.urls
