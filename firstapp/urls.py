from django.conf.urls import url
from firstapp.views import FirstappView

urlpatterns = [
    url(r'^firstapp/', FirstappView.as_view()),
]
