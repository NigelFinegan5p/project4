from . import views
from django.urls import path

urlpatterns = [
    path('gifts/', views.GiftsView.as_view(), name='gifts'),
]


# CI Python Linter 16/01/2025 10.55am