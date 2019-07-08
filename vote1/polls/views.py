from django.shortcuts import render,redirect,reverse
from .models import *
from django.http import *
# Create your views here.


def checklogin(fun):
    def check(request,*args):
        # username = request.COOKIES.get("username")
        username = request.session.get("username")
        if username:
            return fun(request,*args)
        else:
            return redirect(reverse("polls:login"))
    return check

@checklogin
def index(request):
    # username = request.COOKIES.get("username")
    # if username:
    #     question = Question.objects.all()
    #     return render(request,"polls/index.html",locals())
    # else:
    #     return redirect(reverse("polls:login"))
    username = request.session.get("username")
    question = Question.objects.all()
    return render(request, "polls/index.html", locals())

@checklogin
def detail(request,id):
    try:
        question = Question.objects.get(pk=id)
    except Question.DoesNotExist:
        return HttpResponse("id非法")
    except Question.MultipleObjectsReturned:
        return HttpResponse("id非法")
    if request.method == "GET":
        choice = question.choice_set.all()
        return render(request,"polls/detail.html",locals())
    else:
        choiceid = request.POST.get("choice")
        Choice.objects.addvote(choiceid)
        # choice = Choice.objects.get(pk=choiceid)
        # choice.votes += 1
        # choice.save()
        return redirect(reverse("polls:result",args=(id,)))

@checklogin
def result(request,id):
    question = Question.objects.get(pk=id)
    choice = question.choice_set.all()
    return render(request,"polls/result.html",locals())


def login(request):
    if request.method == "GET":
        return render(request,"polls/login.html")
    else:
        #使用cookies
        # response = redirect(reverse("polls:index"))
        # response.set_cookie("username",request.POST.get("username"))
        # return response
        #使用session
        request.session["username"] = request.POST.get("username")
        return redirect(reverse("polls:index"))

def logout(request):
    # res = redirect(reverse("polls:login"))
    # res.delete_cookie("username")
    # return res
    request.session.flush()
    return redirect(reverse("polls:login"))