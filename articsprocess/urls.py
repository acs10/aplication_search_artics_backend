from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import Register, Data

app_name = 'api'

urlpatterns = [
    path(r'register', Register.as_view()),
    path(r'data', Data.as_view()),
    ]

