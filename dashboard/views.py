from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from blog.models import Blog, Category
from django.contrib.auth.decorators import login_required
from dashboard.forms import AddUserFrom, BlogForm, CategoryForm,EditUsers
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


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

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
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
@login_required(login_url='login')
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
@login_required(login_url='login')
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
@login_required(login_url='login')
def PostDelete(request,pk):
    delete = get_object_or_404(Blog,pk=pk)
    delete.delete()
    return redirect('post')

@login_required(login_url='login')
def BlogUser(request):
    users = User.objects.all()
    context = {
        'users' : users
    }
    return render(request,'dashboard/blog_user.html',context)
@login_required(login_url='login')
def AddUser(request):
    if request.method == 'POST':
        form = AddUserFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_user')
    form = AddUserFrom()
    context = {
        'form' : form
    }
    return render(request,'dashboard/add_user.html',context)

def EditUser(request,pk):
    user = get_object_or_404(User,pk=pk)
    if request.method == 'POST':
        form = EditUsers(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('blog_user')
    form = EditUsers(instance=user)
    context = {
        'form' : form,
        'user' : user
    }
    return render(request,'dashboard/edit_user.html',context)

def UserDelete(request,pk):
    delete = get_object_or_404(User,pk=pk)
    delete.delete()
    return redirect('blog_user')