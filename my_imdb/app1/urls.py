from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name='index'),
    path("genre/<str:genre_n>/",views.genres,name='genre'),
    path("shows/<slug:showname>/<slug:season>/",views.shows,name='shows'),
    path("movies/<slug:mname>/",views.movies,name='movies'),
    path("profile/<slug:uname>/",views.profile,name='profile'),
    
]