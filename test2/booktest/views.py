from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("首页 <a href='list/'>跳转到商品页</a>")

def list(request):
    return HttpResponse("商品页 <a href='/detail/'>跳转到详情页</a>")

def detail(request):
    return HttpResponse("详情页 <a href='/'>跳转到首页</a>")