from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('blogpost/<id:int>',views.blogpost,name='Blogpost'),
   
    
   
]