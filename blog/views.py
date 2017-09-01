# Create your views here.
# coding:utf-8
from django.http import HttpResponse

def index(req):
    return HttpResponse(u'<h1>Hello,World!我得世界！</h1>')
# Create your views here.
