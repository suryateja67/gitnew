from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello haritha")
def brian(request):
    return HttpResponse("hello,brian")
def haritha(request):
    return HttpResponse("hai baby, i love you , break up!")
def greet(request,name):
    name=name.upper()
    return HttpResponse(f"hello,{name}!")
def raj(request):
    return render(request,"hello/index.html")
def greet(request,name):
    return render(request,"hello/greet.html",{"name":name.capitalize()})