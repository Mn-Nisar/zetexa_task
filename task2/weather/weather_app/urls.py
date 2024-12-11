from django.contrib import admin
from django.urls import path, include
from .views import report_weather

urlpatterns = [
    path('',report_weather),
]
