from django.contrib import admin
from django.db import models
from .models import BlogPost

# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'time']

admin.site.register(BlogPost, BlogPostAdmin)
