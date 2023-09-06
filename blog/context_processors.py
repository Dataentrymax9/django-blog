from .models import Category

def All_Category(request):
    Categories = Category.objects.all()
    return dict(categories=Categories)