from django.http import HttpResponse
from django.shortcuts import render

def my_firstapp(request):
  return render(request,"firstapp.html")

  



