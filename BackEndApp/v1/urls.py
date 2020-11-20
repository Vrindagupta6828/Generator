from django.contrib import admin
from django.urls import path, include
from . import views
from .views import RegisterAPI,LoginAPI
from knox import views as knox_views

urlpatterns = [
    path('generate/', views.generate, name='generate'),
    path('train/', views.train, name='train'),
    path('compile/', views.compile, name='compile'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
]
