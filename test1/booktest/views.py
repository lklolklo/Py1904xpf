#引入简写模块分别是  响应简写，重定向简写，解除硬编码
from django.shortcuts import render,redirect,reverse

#获取模板的引入
from django.template import loader


#编写响应,重定向
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.



#引入模板
from .models import *


#MVT 中核心V视图
#接受请求，处理数据，返回响应

def index(request):
    # return HttpResponse("首页 <a href='seccend/'>跳转到商品页</a>")
    # #1获取模板
    # temp1 = loader.get_template("booktest/index.html")
    # #2使用模板渲染字典参数
    # resut1 = temp1.render({"username":"xpf"})
    # #3将渲染的结果返回
    # return HttpResponse(resut1)
    return render(request,"booktest/index.html",{"username":"lklo"})



def list(request):
    # return HttpResponse("商品页%s "%(s,))
    # #1获取模板
    # temp2 = loader.get_template("booktest/list.html")
    # books = BookInfo.objects.all()
    #
    # #2使用模板渲染字典参数
    # resut2 = temp2.render({"books":books})
    # #3将渲染的结果返回
    # return HttpResponse(resut2)
    books = BookInfo.objects.all()
    return render(request,"booktest/list.html",{"books":books})



def detail(request,id):
    # return HttpResponse("%s详情页<a href='/'>跳转到首页</a>"%id)
    # #1获取模板
    # temp3 = loader.get_template("booktest/detail.html")
    # book = BookInfo.objects.get(pk=id)
    # #2使用模板渲染字典参数
    # resut3 = temp3.render({"book":book})
    # #3将渲染的结果返回
    # return HttpResponse(resut3)
    book = BookInfo.objects.get(pk=id)
    return render(request,"booktest/detail.html",{"book":book})


def addb(request):
    # return HttpResponse("书籍添加成功")
    if request.method == "GET":
        return render(request,"booktest/addb.html")
    elif request.method == "POST":
        title = request.POST.get("title")
        book = BookInfo()
        book.title = title
        book.save()
        return redirect(reverse("booktest:list"))


def delb(request,id):
    book = BookInfo.objects.get(pk=id)
    book.delete()

    return redirect(reverse("booktest:list"))
    # return HttpResponse("删除成功")


def addh(request,id):
    # return HttpResponse("ok")
    book = BookInfo.objects.get(pk=id)

    if request.method == "GET":
        return render(request,"booktest/addh.html",{"book":book})
    elif request.method == "POST":
        name = request.POST.get("username")
        content = request.POST.get("content")
        gender = request.POST.get("gender")
        HeroInfo.objects.addhero(name,content,gender,book)
        # hero = HeroInfo()
        # hero.name = name
        # hero.content = content
        # hero.gender = gender
        # hero.book = book
        # hero.save()
        return redirect(reverse("booktest:detail",args=(id,)))




def delt(request,id):
    hero = HeroInfo.objects.get(pk=id)
    bookid = hero.book.id
    hero.delete()
    # return HttpResponse("删除成功")
    # return HttpResponseRedirect("/detail/%s/"%(bookid,))
    result = reverse("booktest:detail",args=(bookid,))
    return redirect(result)