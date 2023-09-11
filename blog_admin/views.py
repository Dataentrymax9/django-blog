from django.http import HttpResponse
from django.shortcuts import redirect, render
from about.models import About
from blog.models import Blog, Category
from .forms import RegistractionForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def Home(request):
    feature_post = Blog.objects.filter(is_featured=True,status='Published').order_by('-update_at')
    s_post = Blog.objects.filter(is_featured=False,status='Published')
    about = About.objects.get()
    context = {
        'feature_post' : feature_post,
        'simple' : s_post,
        'about' : about,
    }
    return render(request,'index.html',context)

def Register(request):
    if request.method == "POST":
        form =RegistractionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =RegistractionForm()
    context = {
        'form' : form
    }
    return render(request,'register.html',context)

def Login(request):
    if request.user.is_authenticated:
      return redirect('dashboard')  
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
            return redirect('dashboard')
    form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request,'login.html',context)

def Logout(request):
    auth.logout(request)
    return redirect('home')