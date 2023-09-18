from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Category(models.Model):
    category_name = models.CharField(max_length=50,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.category_name

STATUS_CHOICES = (
    ('Draft',"Draft"),
    ('Published',"Published")
)

class Blog(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique=True,blank=True)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_desc = models.TextField(max_length=500)
    blog_body = HTMLField()
    status = models.CharField(max_length=30,choices=STATUS_CHOICES,default="Draft")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment = models.TextField(max_length=250,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
    