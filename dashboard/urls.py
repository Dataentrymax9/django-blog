from django.urls import path
from . import views
urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    #Category Curd
    path('categories/',views.Dcategories,name='dcategories'),
    path('categories/add',views.AddCategories,name='add_categories'),
    path('categories/edit/<int:pk>/',views.EditCategories,name='edit_categories'),
    path('categories/delete/<int:pk>/',views.DeleteCategories,name='delete_categories'),
    #Blog Post Crud
    path('post/',views.Post,name='post'),
    path('post/add',views.PostAdd,name='postadd'),
    path('post/edit/<int:pk>/',views.EditPost,name='edit_post'),
    path('post/delete/<int:pk>/',views.PostDelete,name='post_delete')

]
