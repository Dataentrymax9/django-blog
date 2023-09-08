from about.models import SocialLink
from .models import Category

def All_Category(request):
    Categories = Category.objects.all()
    return dict(categories=Categories)

def get_all_sociallink(request):
    sociallink = SocialLink.objects.all()
    return dict(sociallink=sociallink)