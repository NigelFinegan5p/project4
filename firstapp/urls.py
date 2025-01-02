from . import views
from django.urls import path

urlpatterns = [
    path('', views.FirstappView.as_view(), name='home'),
]



# from django.conf.urls import url
# from firstapp.views import FirstappView
# url(r'^firstapp/', FirstappView.as_view()),