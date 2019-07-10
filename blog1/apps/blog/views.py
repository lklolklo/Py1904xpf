from django.shortcuts import render,redirect,reverse
from django.views.generic import View
from django.http import HttpResponse
from .models import *
from .forms import ArticleForm
from django.core.paginator import Paginator,Page
# Create your views here.


class IndexView(View):
    def get(self,request):
        ads = Ads.objects.all()
        articles = Article.objects.all()
        # paginator = Paginator(articles,1)
        # print(paginator.page_range)
        # print(paginator.object_list)
        # print(paginator.num_pages)
        # print(paginator.count)
        # page = paginator.get_page(2)
        # print(page)
        # print(page.paginator)
        # print(page.object_list)
        # print(page.number)
        # print(page.next_page_number())
        # print(page.previous_page_number())
        # print(page.has_next())
        # print(page.has_previous())
        pagenum = request.GET.get("page")
        pagenum = 1 if not pagenum else pagenum
        page = Paginator(articles,1).get_page(pagenum)
        return render(request,"blog/index.html",locals())


class SingleView(View):
    def get(self,request,id):
        article = Article.objects.all()
        return render(request,"blog/single.html")
    def post(self,request,id):
        return render(request,"blog.single.html")

class AddArticleView(View):
    def get(self,request):
        af = ArticleForm()
        return render(request,"blog/addarticle.html",locals())
    def post(self,request):
        af = ArticleForm(request.POST)
        if af.is_valid():
            article = af.save(commit=False)
            article.category = Category.objects.first()
            article.author = User.objects.first()
            article.save()
            return redirect(reverse("blog:index"))
        return HttpResponse("ok")