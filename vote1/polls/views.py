from django.shortcuts import render,redirect,reverse
from .models import *
from django.http import *
# Create your views here.


def index(request):
    question = Question.objects.all()
    return render(request,"polls/index.html",locals())

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

def result(request,id):
    question = Question.objects.get(pk=id)
    choice = question.choice_set.all()
    return render(request,"polls/result.html",locals())