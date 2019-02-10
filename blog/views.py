from django.shortcuts import render
from .models import BlogPost



# Create your views here.


def index(request):
    posts = BlogPost.objects.all()

    context = {'posts': posts}
    return render(request, 'blog/index.html', context)

