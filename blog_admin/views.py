from django.http import HttpResponse
from django.shortcuts import render
from about.models import About
from blog.models import Blog, Category

def Home(request):
    feature_post = Blog.objects.filter(is_featured=True,status='Published').order_by('update_at')
    s_post = Blog.objects.filter(is_featured=False,status='Published')
    about = About.objects.get()
    context = {
        'feature_post' : feature_post,
        'simple' : s_post,
        'about' : about,
    }
    return render(request,'index.html',context)