from django.shortcuts import render,redirect,reverse
from .models import *
from django.http import *
# Create your views here.
from django.contrib.auth import login as lgi ,logout as lgo,authenticate

def checklogin(fun):
    def check(request,*args):
        # username = request.COOKIES.get("username")
        # username = request.session.get("username")
        # if username:
        if request.user and request.user.is_authenticated:
            return fun(request,*args)
        else:
            return redirect(reverse("polls:login"))
    return check

@checklogin
def index(request):
    #1.cookies
    # username = request.COOKIES.get("username")
    # if username:
    #     question = Question.objects.all()
    #     return render(request,"polls/index.html",locals())
    # else:
    #     return redirect(reverse("polls:login"))
    #2.session
    # username = request.session.get("username")
    # question = Question.objects.all()
    # return render(request, "polls/index.html", locals())
    #3.自带的三种授权
    questions = Question.objects.all()
    return render(request,"polls/index.html",{"questions":questions})


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
        # Choice.objects.addvote(choiceid)
        choice = Choice.objects.get(pk=choiceid)
        choice.votes += 1
        choice.save()
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
        # request.session["username"] = request.POST.get("username")
        # return redirect(reverse("polls:index"))
        #3
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username = username,password=password)
        if user:
            lgi(request,user)
            return redirect(reverse("polls:index"))
        else:
            return render(request, 'polls/login.html', {"errors": "登录失败"})



def logout(request):
    #1
    # res = redirect(reverse("polls:login"))
    # res.delete_cookie("username")
    # return res
    #2
    # request.session.flush()
    #3
    lgo(request)
    return redirect(reverse("polls:login"))

def regist(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = PollsUser.objects.create_user(username=username,password=password)
        except:
            user = None

        if user:
            return redirect(reverse("polls:login"))
        else:
            return render(request,"polls/login/html",{"errors":"注册失败"})