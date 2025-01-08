"""
URL configuration for codestar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from firstapp.views import my_firstapp
# from django.conf.urls import url
from django.urls import re_path as url
# from django.views.generic import TemplateView
from firstapp.views import FirstappView
from about import views as about_views
from hello_world import views as index_views
# gift app added for gifts page (views)
from django.urls import re_path as url
from gifts.views import GiftsView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls')),
    
    path('', include("firstapp.urls"), name='home'),
    # path('about/', about_views.about_me, name='about'),
    path("about/", include("about.urls"), name="about-urls"),
    # path('hello/', index_views.index, name='index'),
    path("blog/", include("blog.urls"), name="blog-urls"),
    path("gifts/", include("gifts.urls"), name='gifts'),
    path('hello/', include('hello_world.urls')),
]

# path('', TemplateView.as_view(template_name="firstapp.html")),