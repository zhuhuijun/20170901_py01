# Create your views here.
# coding:utf-8
from django.http import HttpResponse
from people.models import Person
from django.shortcuts import render_to_response

def index(req):
    #return HttpResponse(u'<h1>Hello,World!我得世界！</h1>')
    return render(req, 'default.html')

def myindex(req):
    #return HttpResponse(u'<h1>Hello,World!我得世界！</h1>')
    peoples = Person.objects.all()
    return render_to_response('default.html',{'peoples':peoples})

def myindex2(req):
    #return HttpResponse(u'<h1>Hello,World!我得世界！</h1>')
    peoples = Person.objects.all()
    return render_to_response('default1.html',{'peoples':peoples})

