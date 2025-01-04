from . import views
from django.urls import path

urlpatterns = [
    path('gifts/', views.GiftsView.as_view(), name='gifts'),
]



