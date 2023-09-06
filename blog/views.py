from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, Category


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
    
