from django.shortcuts import render

#获取模板的引入
from django.template import loader


#编写响应
from django.http import HttpResponse
# Create your views here.



#引入模板
from .models import Book,Hero


#MVT 中核心V视图
#接受请求，处理数据，返回响应

def index(request):

    return render(request,"booktest/index.html",{"username":"lklo"})



def list(request):

    books = Book.objects.all()
    return render(request,"booktest/list.html",{"books":books})



def detail(request,id):

    book = Book.objects.get(pk=id)
    return render(request,"booktest/detail.html",{"book":book})