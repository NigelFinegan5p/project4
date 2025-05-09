from . import views
from django.urls import path

urlpatterns = [
    path('', views.FirstappView.as_view(), name='home'),
]


# CI Python Linter 16/01/2025 10.35am