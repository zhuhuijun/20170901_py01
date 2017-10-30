# Create your views here.
# coding:utf-8
from django.http import HttpResponse
from blog.models import Student
from django.shortcuts import render

def index(req):
    return HttpResponse(u'<h1>Hello,World!我得世界！</h1>')
# Create your views here.
def default(req):
    stu1 = Student(name='rt')
    stu1.save()
    students = Student.objects.all()
    return render_to_response('default.html',{'students':students})

