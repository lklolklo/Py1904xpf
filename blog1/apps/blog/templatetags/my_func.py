from django.template import library
#自定义模板表达式，扩展django原有功能
from blog.models import Article,Category,Tag,Ads

register = library.Library()

@register.simple_tag
def getads():
    return Ads.objects.all()



@register.simple_tag
def getlatestarticles(num=4):
    return Article.objects.order_by("-create_time")[:num]


@register.simple_tag
def gettimes():
    times = Article.objects.dates("create_time","month","DESC")
    # print(times)
    return times




@register.simple_tag
def getcategorys():
    return Category.objects.all()

@register.simple_tag
def gettags():
    return Tag.objects.all()







@register.filter
def mylower(value):
    return value.lower()

@register.filter
def myjoin(value,spl):
    return spl.join(value)