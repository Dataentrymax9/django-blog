from django import forms
from blog.models import Blog, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','Category','featured_image','short_desc','blog_body','status','is_featured')
