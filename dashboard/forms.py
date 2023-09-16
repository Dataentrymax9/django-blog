from django import forms
from blog.models import Blog, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','Category','featured_image','short_desc','blog_body','status','is_featured')

class AddUserFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','is_active','is_staff')

class EditUsers(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','is_active','is_staff')