from . import views
from django.urls import path

urlpatterns = [
    path('', views.about_me, name='about'),
]

# CI Python Linter 15/01/2025  16.48pm