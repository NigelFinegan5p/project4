from . import views
from django.urls import path

urlpatterns = [
    path('firstapp/', my_firstapp, name='firstapp'),
]

