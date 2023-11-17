from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('view/',views.ViewPost,name ='view'),
    path('add/',views.AddPost,name ='add'),
    path('search/',views.SearchPost,name ='search'),
    
]


