from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, Category
from django.db.models import Q


def CategoryPost(request,cat_id):
    #Fatch the post that belong the category with the category_id 
    cate_post = Blog.objects.filter(status='Published',Category_id=cat_id)
    try:
        category = Category.objects.get(pk=cat_id)
    except:
        return redirect('home')
    #category = get_object_or_404(Category,pk=cat_id)
    context = {
        "post" : cate_post,
        'category' : category
    }
    return render(request,'category.html',context)
    
def blog(request,b_slug):
    single_blog = get_object_or_404(Blog,slug=b_slug)
    context = {
        "Sblog" : single_blog
    }
    return render(request,'single_blog.html',context)

def search(request):
    keyword = request.GET.get('keyword')
    blog = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_desc__icontains = keyword),status='Published')
    context = {
        'blog' : blog,
        'keyword' : keyword
    }
    return render(request,'search.html',context)