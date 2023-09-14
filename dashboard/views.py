from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from blog.models import Blog, Category
from django.contrib.auth.decorators import login_required
from dashboard.forms import BlogForm, CategoryForm
from django.template.defaultfilters import slugify


@login_required(login_url='login')
def dashboard(request):
    all_categories = Category.objects.all().count()
    all_blog = Blog.objects.all().count()
    context = {
        'ca_count' : all_categories,
        'blog_count' : all_blog,
    }
    return render(request,'dashboard/dashboard.html',context)

def Dcategories(request):
    return render(request,'dashboard/categories.html')

def AddCategories(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dcategories')
    form = CategoryForm()
    context = {
        'form' : form
    }
    return render(request,'dashboard/add_categories.html',context)

def EditCategories(request,pk):
    category = get_object_or_404(Category,pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('dcategories')
    form = CategoryForm(instance=category)
    context = {
        'form' : form,
        'category' : category
    }
    return render(request,'dashboard/edit_categories.html',context)

def DeleteCategories(request,pk):
    category = get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('dcategories')

def Post(request):
    post = Blog.objects.all()
    context = {
        'post' : post
    }
    return render(request,'dashboard/post.html',context)

def PostAdd(request):
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False) #Tempory save the data
            post.author = request.user
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title)+'-'+str(post.id)
            post.save()
            return redirect('post')
    form = BlogForm()
    context = {
        'form' : form
    }
    return render(request,'dashboard/post_add.html',context)

def EditPost(request,pk):
    post = get_object_or_404(Blog,pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug =slugify(title)+'-'+str(post.id)
            post.save()
            return redirect('post')
    form = BlogForm(instance=post)
    context = {
        'form' : form,
        'post' : post
    }
    return render(request,'dashboard/post_edit.html',context)

def PostDelete(request,pk):
    delete = get_object_or_404(Blog,pk=pk)
    delete.delete()
    return redirect('post')