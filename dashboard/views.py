from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from blog.models import Blog, Category
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm

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