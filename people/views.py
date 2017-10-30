# Create your views here.
# coding:utf-8
from django.http import HttpResponse
from people.models import Person
from django.shortcuts import render

def index(req):
    #return HttpResponse(u'<h1>Hello,World!我得世界！</h1>')
    return render(req, 'default.html')

def default(req):
    peoples = Person.objects.all()
    return render_to_response('default.html',{'peoples':peoples})
