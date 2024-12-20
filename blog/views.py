from django.shortcuts import render
# from django.http import HttpResponse
from django.views import generic
from .models import Post


# Create your views here.
class PostList(generic.ListView):
    # model = Post
    queryset = Post.objects.all().filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6
    
    # template_name = "post_list.html"

# def my_blog(request):
#     return HttpResponse("Hello, Blog!")

        

