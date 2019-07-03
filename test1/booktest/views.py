from django.shortcuts import render

#编写响应
from django.http import HttpResponse
# Create your views here.

#MVT 中核心V视图
#接受请求，处理数据，返回响应

def first(request):
    return HttpResponse("首页 <a href='/booktest/seccend/'>跳转到商品页</a>")

def seccend(request):
    return HttpResponse("商品页<a href='/booktest/third/'>跳转到详情页</a>")

def third(request):
    return HttpResponse("详情页<a href='/booktest/first/'>跳转到首页</a>")