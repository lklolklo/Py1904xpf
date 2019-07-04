from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Ques,Count
# Create your views here.

def list(request):
    # return HttpResponse("问题列表")
    question = Ques.objects.all()
    return render(request, "votetest/list.html", {"question": question})



def answer(request,id):
    ques = Ques.objects.get(pk=id)
    return render(request, "votetest/anwser.html",{"ques":ques})


def result(request,id):
    pass