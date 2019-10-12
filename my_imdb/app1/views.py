from django.shortcuts import render
from django.http import HttpResponse
from .models import User,Genre,Comments


def index(request):
    return render(request,"index.html")

def shows(request,showname,season):
    site = showname +"-"+season+".html"
    return render(request,site)

def genres(request,genre_n):
    site = genre_n + ".html"
    c = Comments.objects.filter(genre__genre_name__contains=genre_n)
    return render(request,site,{'c':c})

def movies(request,mname):
    site = mname + ".html"
    return render(request,site)

def profile(request,uname):
    u = User.objects.get(username=uname)
    return render(request,'user.html',{'u':u})

