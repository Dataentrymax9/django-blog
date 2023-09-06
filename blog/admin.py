from django.contrib import admin
from .models import Category
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
    list_display = ('title','Category','author','status','is_featured')
    search_fields = ('title','status','Category__category_name')
    list_editable = ("is_featured","Category","status","author")


admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)
