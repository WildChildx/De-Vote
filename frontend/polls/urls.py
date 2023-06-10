from django.urls import path 

# import all views from current folder
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vote',views.vote,name = 'vote')
]