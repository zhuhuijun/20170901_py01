# Create your views here.
# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render

def index(req):
    #return HttpResponse(u'<h1>Hello,World!我得世界！</h1>')
    return render(req, 'home.html')
# Create your views here.
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request,a,b):
    c = int(a)+int(b)
    return HttpResponse(str(c))