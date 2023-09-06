from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Blog, Category

def Home(request):
    feature_post = Blog.objects.filter(is_featured=True,status='Published').order_by('update_at')
    s_post = Blog.objects.filter(is_featured=False,status='Published')
    context = {
        'feature_post' : feature_post,
        'simple' : s_post
    }
    return render(request,'index.html',context)