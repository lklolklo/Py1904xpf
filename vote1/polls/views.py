from django.shortcuts import render,redirect,reverse,get_object_or_404
from .models import *
from django.http import *
from PIL import Image,ImageDraw,ImageFont
import random,io
# Create your views here.
from django.contrib.auth import login as lgi ,logout as lgo,authenticate
from .forms import *
from django.core.cache import cache
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
from itsdangerous import TimedJSONWebSignatureSerializer

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


# def login(request):
#     if request.method == "GET":
#         lgf = LoginForm()
#         # print(lgf)
#         return render(request,"polls/login.html",{"lgf":lgf})
#     else:
#         #使用cookies
#         # response = redirect(reverse("polls:index"))
#         # response.set_cookie("username",request.POST.get("username"))
#         # return response
#         #使用session
#         # request.session["username"] = request.POST.get("username")
#         # return redirect(reverse("polls:index"))
#         #3
#         # username = request.POST.get("username")
#         # password = request.POST.get("password")
#         lgf = LoginForm(request.POST)
#         if lgf.is_valid():
#             username = lgf.cleaned_data["username"]
#             password = lgf.cleaned_data["password"]
#         user = authenticate(request,username = username,password=password)
#         if user:
#             lgi(request,user)
#             return redirect(reverse("polls:index"))
#         else:
#             return render(request, 'polls/login.html', {"errors": "登录失败"})

def login(request):
    lgf = LoginForm()
    rgf = RegistForm()
    if request.method == "GET":



        return render(request,'polls/login.html',{"lgf":lgf,"rgf":rgf})
    elif request.method == "POST":
        # username = request.POST.get("username")
        # password = request.POST.get("password")

        verifycode = request.POST.get("verify")

        if not verifycode.lower() == cache.get("verify").lower():
            return render(request, 'polls/login.html', {"errors": "验证码错误", "lgf": lgf, "rgf": rgf})

        lgf = LoginForm(request.POST)
        # print(lgf.is_valid())
        if lgf.is_valid():
            username = lgf.cleaned_data["username"]
            password = lgf.cleaned_data["password"]
            # print("***************")
            # print(username)
            # print(password)
            # user = authenticate(request,username=username,password=password)
            # user = PollsUser.objects.filter(username=username).first()
        #     user = PollsUser.objects.filter(username=username).first()
        #     if user.check_passwork(password):
        #         if user:
        #             if user.is_active:
        #                 lgi(request,user)
        #                 return redirect(reverse("polls:index"))
        #             else:
        #                 return render(request, 'polls/login.html', {"errors": "登录失败,用户未激活", "lgf": lgf, "rgf": rgf})
        #         else:
        #             return render(request, 'polls/login.html', {"errors": "登录失败，账号或密码错误","lgf":lgf,"rgf":rgf})
        #     else:
        #         return render(request, 'polls/login.html', {"errors": "登录失败,密码错误", "lgf": lgf, "rgf": rgf})
        # else:
        #     return render(request, 'polls/login.html', {"errors": "登录失败","lgf":lgf,"rgf":rgf})
            user = PollsUser.objects.filter(username=username).first()
            if user.check_password(password):
                print(user)
                if user:
                    if user.is_active:


                        lgi(request,user)
                        return redirect(reverse("polls:index"))
                    else:
                        return render(request, 'polls/login.html', {"errors": "账户尚未激活", "lgf": lgf, "rgf": rgf})
                else:
                    print("----")
                    return render(request, 'polls/login.html', {"errors": "登录失败","lgf":lgf,"rgf":rgf})
            else:
                return render(request, 'polls/login.html', {"errors": "密码错误", "lgf": lgf, "rgf": rgf})
        else:
            print("++++")
            return render(request, 'polls/login.html', {"errors": "登录失败","lgf":lgf,"rgf":rgf})

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

# def regist(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#
#         try:
#             user = PollsUser.objects.create_user(username=username,password=password)
#         except:
#             user = None
#
#         if user:
#             return redirect(reverse("polls:login"))
#         else:
#             return render(request,"polls/login/html",{"errors":"注册失败"})
def regist(request):
    if request.method == "POST":
        rgf = RegistForm(request.POST)
        if rgf.is_valid():
            # 先返回一个user 此时没有保存数据库应为密码还没有加密
            user = rgf.save(commit=False)
            # 对user用户设置密码 加密过得密码
            user.set_password(rgf.cleaned_data["password"])

            #设置用户状态未激活
            user.is_active = False

            # 保存数据库
            user.save()


            recvlist = [request.POST.get("email")]
            print(recvlist)

            serializer = TimedJSONWebSignatureSerializer(settings.SECRET_KEY)
            serializerstr = serializer.dumps({"userid": user.id}).decode("utf-8")

            try:
                # send_mail("测试","这是测试邮件",settings.EMAIL_HOST_USER,recvlist)
                mail = EmailMultiAlternatives("注册激活", "<h1><a href='http://127.0.0.1:8000/active/%s/'>点此激活</a></h1>"%(serializerstr,),
                                              settings.EMAIL_HOST_USER, recvlist)
                mail.content_subtype = "html"
                mail.send()
                print("ok")
            except Exception as e:
                print(e)

            return redirect(reverse("polls:login"))
        else:
            lgf = LoginForm()
            rgf = RegistForm()
            return render(request, 'polls/login.html', {"errors": "注册失败","lgf":lgf,"rgf":rgf})

        # username =request.POST.get("username")
        # password = request.POST.get("password")
        #
        # try:
        #     user = PollsUser.objects.create_user(username=username, password=password)
        # except:
        #     user = None
        #
        # if user:
        #     return redirect(reverse("polls:login"))
        # else:
        #     return render(request, 'polls/login.html', {"errors":"注册失败"})

    else:
        return HttpResponse("错误")


def checkuser(request):
    if request.method == "GET":
        name = request.GET.get("name")
        qs = PollsUser.objects.filter(username=name)
        user = qs.first()
        if user:
            return JsonResponse({"state":1})
        else:
            return JsonResponse({"state":0,'errorinfo':"用户名不存在"})




def verify(request):
    bgcolor = (random.randrange(20, 100),
               random.randrange(20, 100),
               random.randrange(20, 100))
    width = 100
    heigth = 35
    # 创建画面对象
    im = Image.new('RGB', (width, heigth), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, heigth))
    fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
    draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    print("验证码为：", rand_str)
    # rand_str = rand_str.lower()
    cache.set("verify",rand_str)
    # 构造字体对象
    font = ImageFont.truetype('BRLNSR.TTF', 23)
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # request.session['verifycode'] = rand_str
    f = io.BytesIO()
    im.save(f, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(f.getvalue(), 'image/png')


def active(request,id):
    serializer = TimedJSONWebSignatureSerializer(settings.SECRET_KEY)
    serializerobj = serializer.loads(id)
    id = serializerobj["userid"]

    user = get_object_or_404(PollsUser,pk=id)
    user.is_active=True
    user.save()
    return redirect(reverse('polls:login'))