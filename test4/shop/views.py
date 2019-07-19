from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import *
from django.contrib.auth import login as lgi ,logout as lgo,authenticate
from .forms import *
import random,io
from django.core.cache import cache
from PIL import Image,ImageDraw,ImageFont
from django.core.mail import send_mail,EmailMultiAlternatives
from itsdangerous import TimedJSONWebSignatureSerializer
from django.conf import settings
from django.core.paginator import Paginator,Page
# Create your views here.


def getpage(request,object_list,per_num):
    pagenum = request.GET.get("page")
    pagenum = 1 if not  pagenum else pagenum
    page = Paginator(object_list,per_num).get_page(pagenum)
    return page

def checklogin(fun):
    def check(request,*args):
        if request.user and request.user.is_authenticated:
            return fun(request, *args)
        else:
            return redirect(reverse("shop:login"))

    return check



def index(request):
    return render(request,"shop/index.html",locals())


def list(request):
    foods = Foods.objects.all()

    page = getpage(request,foods,6)
    return render(request,"shop/list.html",locals())


@checklogin
def detail(request,id):
    food = Foods.objects.get(pk=id)

    comment = food.comment_set.all()

    user = PollsUser.objects.get(pk=request.user.id)

    c = Order1.objects.filter(user=user)

    list = []
    for i in c:
        if Order2.objects.filter(order=i, food=food).first():
            list.append(i)

    return render(request,"shop/detail.html",locals())

def login(request):
    lgf = LoginForm()
    if request.method == "GET":

        return render(request,"shop/login.html",{"lgf":lgf})
    else:
        verifycode = request.POST.get("verify")
        print(verifycode)

        if not verifycode.lower() == cache.get("verify").lower():
            return render(request, 'shop/login.html', {"errors": "验证码错误", "lgf": lgf})

        # lgf = LoginForm(request.POST)
        # print(lgf)


        # if lgf.is_valid():
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(password)

        user = PollsUser.objects.filter(username=username).first()
        if user.check_password(password):
            print(user)
            if user:
                if user.is_active:

                    lgi(request,user)
                    return redirect(reverse("shop:index"))
                else:
                    return render(request, 'shop/login.html', {"errors": "账户尚未激活", "lgf": lgf})
            else:
                print("----")
                return render(request, 'shop/login.html', {"errors": "登录失败","lgf":lgf})
        else:
            return render(request, 'shop/login.html', {"errors": "密码错误", "lgf": lgf})
        # else:
        #     print('++++')
        #     print(lgf.errors)
        #     print("++++")
        #     return render(request, 'shop/login.html', {"errors": "登录失败","lgf":lgf})


def register(request):
    rgf = RegistForm()
    if request.method == "GET":
        return render(request,"shop/register.html",{"rgf":rgf})
    else:
        rgf = RegistForm(request.POST)
        if rgf.is_valid():
            print(request.POST.get("password"))
            print(request.POST.get("repeatpassword"))
            if request.POST.get("password") == request.POST.get("repeatpassword"):
                user = rgf.save(commit=False)
                user.set_password(rgf.cleaned_data["password"])
                user.is_active = False
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
                return redirect(reverse("shop:login"))
            else:
                rgf = RegistForm()
                return render(request, 'shop/register.html', {"errors": "两次密码不一致", "rgf": rgf})
        else:
            rgf = RegistForm()
            return render(request, 'shop/register.html', {"errors": "注册失败","rgf":rgf})

def logout(request):
    lgo(request)
    return redirect(reverse("shop:login"))

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
    cache.set("verify", rand_str)
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
    return redirect(reverse('shop:login'))

def FAQ(request):
    return render(request,"shop/FAQ.html")



def about_us(request):
    return render(request,"shop/about_us.html")


def colors(request,id):
    color = get_object_or_404(Color,pk=id)
    foods = color.foods_set.all()
    page = getpage(request,foods,3)
    return render(request,'shop/list.html',locals())


def tags(request,id):
    tag = get_object_or_404(Tag,pk=id)
    foods = tag.foods_set.all()
    page = getpage(request,foods,3)
    return render(request,'shop/list.html',locals())


@checklogin
def incart(request,id):
    userid = request.user.id
    user = PollsUser.objects.get(pk=userid)
    food = Foods.objects.get(pk=id)
    print(user)
    print(food)
    carts = Cart.objects.filter(user=user, foods=food).first()
    print(carts, type(carts))
    if carts:
        s = request.GET.get("number")
        s = int(s)
        carts.number += s
        carts.save()
        return redirect(reverse("shop:cart"))
    else:
        cart = Cart()
        cart.user = user
        cart.foods = food
        s = request.GET.get("number")
        s = int(s)
        cart.number = s
        print(s,type(s))
        cart.save()
        return redirect(reverse("shop:cart"))

@checklogin
def cart(request):
    user = PollsUser.objects.get(pk=request.user.id)
    print(user)
    carts = user.cart_set.all()

    c1 = carts.first()

    total = 0
    for c in carts:
        c.total = c.foods.price2 * c.number
        total += c.total

    return render(request,'shop/cart.html',locals())


def number(request,id):
    number = request.POST.get("number")
    print(number)
    user = PollsUser.objects.get(pk=request.user.id)
    print(user)
    food = Foods.objects.get(pk=id)
    print(food)

    nowtotal = request.POST.get("nowtotal")

    carts = Cart.objects.filter(user=user, foods=food).first()
    print(carts,type(carts))

    nowtotal = int(nowtotal) - carts.number*carts.foods.price2

    carts.number = int(number)
    total = int(number)*carts.foods.price2
    print(total)

    nowtotal += total

    carts.save()


    return JsonResponse({"total":total,"nowtotal":nowtotal})



def delfood(request,id):
    user = PollsUser.objects.get(pk=request.user.id)
    print(user)
    food = Foods.objects.get(pk=id)
    print(food)

    # print("%%%%%%%%%%%%%")
    print(Cart.objects.filter(user=user,foods=food))
    Cart.objects.filter(user=user,foods=food).delete()


    return JsonResponse({"number": "111"})


def inorder(request):
    # print('inore')
    user = PollsUser.objects.get(pk=request.user.id)

    o1 = Order1()
    o1.user = user
    o1.save()

    carts = user.cart_set.all()

    nowtotal = 0
    for c in carts:
        c.id = Order2()
        c.id.order = o1
        c.id.food = c.foods
        c.id.number = c.number

        total = c.number*c.foods.price2

        nowtotal += total
        c.id.total = total

        c.id.save()

    user.cart_set.all().delete()

    o1.total = nowtotal
    o1.save()

    return redirect(reverse("shop:order"))


@checklogin
def order(request):
    user = PollsUser.objects.get(pk=request.user.id)

    order1 = user.order1_set.all()

    o1 = order1.first()

    return render(request,"shop/order.html",locals())


def addcomment(request,id):
    user = PollsUser.objects.get(pk=request.user.id)
    food = Foods.objects.get(pk=id)
    comment = Comment()
    comment.user = user
    comment.food = food
    comment.content = request.POST.get("content")
    comment.save()

    return redirect(reverse("shop:detail",args=(id,)))