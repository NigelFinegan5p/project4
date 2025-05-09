from django.urls import path
from . import views

urlpatterns = [
    path('', views.giftbox_list, name='giftbox_list'),
    path('book/<int:giftbox_id>/', views.book_giftbox, name='book_giftbox'),
    path('booking_confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
]

# CI Python Linter 16/01/2025 11.24am