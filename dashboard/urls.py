from django.urls import path
from . import views
urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('categories/',views.Dcategories,name='dcategories'),
    path('categories/add',views.AddCategories,name='add_categories'),
    path('categories/edit/<int:pk>/',views.EditCategories,name='edit_categories'),
    path('categories/delete/<int:pk>/',views.DeleteCategories,name='delete_categories'),
]
