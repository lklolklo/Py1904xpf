from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import Ques,Count
# Create your views here.

def list(request):
    # return HttpResponse("问题列表")
    question = Ques.objects.all()
    return render(request, "votetest/list.html", {"question": question})



def answer(request,id):

    if request.method == "GET":
        # return HttpResponse("1111")
        ques = Ques.objects.get(pk=id)
        # print(ques)
        return render(request, "votetest/answer.html", {"ques": ques})
    elif request.method == "POST":
        ques = Ques.objects.get(pk=id)
        count = Count.objects.get(question=ques)
        option = request.POST.get("count")
        print(option,type(option))
        if option == "1":
            count.opt1 += 1
        elif option == "2":
            count.opt2 += 1
        elif option == "3":
            count.opt3 += 1
        else:
            count.opt4 += 1
        count.save()
        return redirect(reverse("votetest:result",args=(count.id,)))
        # return render(request,"votetest/result.html")




def result(request,id):
    count = Count.objects.get(pk=id)
    ques = count.question
    return render(request, "votetest/result.html", locals())

