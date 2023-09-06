from django.urls import path
from . import views

urlpatterns = [
    path('<int:cat_id>',views.CategoryPost,name='CategoryPost')
]
