from django.shortcuts import render,redirect,reverse
from .models import *
# Create your views here.


def index(request):
    question = Question.objects.all()
    return render(request,"polls/index.html",locals())

def detail(request,id):
    pass

def result(request,id):
    pass