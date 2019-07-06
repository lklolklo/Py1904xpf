from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
# Create your views here.
from .models import *

def index(request):
    return render(request,"booktest/index.html",{"username":"lklo"})

def list(request):
    book = Book.objects.all()
    return render(request,"booktest/list.html",{"books":book})

def detail(request,id):
    book = Book.objects.get(pk=id)
    hero = book.hero_set.all()
    return render(request,"booktest/detail.html",locals())

def addbook(request):
    if request.method == "GET":
        return render(request,"booktest/addbook.html")
    else:
        title = request.POST.get("title")
        book = Book()
        book.title = title
        book.save()
        return redirect(reverse("booktest:list"))

def delbook(request,id):
    book = Book.objects.get(pk=id)
    book.delete()
    return redirect(reverse("booktest:list"))

def addhero(request,id):
    book = Book.objects.get(pk=id)
    # return HttpResponse("1111")
    # if request.method == "GET":
    if request.method == "GET":
        return render(request, "booktest/addhero.html", {"book": book})
    else:
        name = request.POST.get("heroname")
        gender = request.POST.get("gender")
        content = request.POST.get("content")
        Hero.objects.addhero(name,gender,content,book)
        # hero = Hero()
        # hero.name = name
        # hero.gender = gender
        # hero.content = content
        # hero.book = book
        # hero.save()
        return redirect(reverse("booktest:detail",args=(id,)))

def delhero(request,id):
    hero = Hero.objects.get(pk=id)
    bookid = hero.book.id
    hero.delete()
    return redirect(reverse("booktest:detail",args=(bookid,)))
