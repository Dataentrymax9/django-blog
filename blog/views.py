from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, Category, comment
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
    #cmments
    if request.method == "POST":
        comments = comment()   
        comments.user = request.user
        comments.blog = single_blog
        comments.comment = request.POST['comment']
        comments.save()
        return HttpResponseRedirect(request.path_info)
    comments = comment.objects.filter(blog=single_blog)
    count = comments.count()
    context = {
        "Sblog" : single_blog,
        'comments' : comments,
        'count' : count
    }
    return render(request,'single_blog.html',context)

def search(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword')
        if keyword != None:
            blog = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_desc__icontains = keyword),status='Published')
        if keyword == "":
            return render(request,"search.html",{"error":True})   
    context = {
        'blog' : blog,
        'keyword' : keyword
    }
    return render(request,'search.html',context)