from django.template import library
from shop.models import *
register = library.Library()


@register.simple_tag
def getcolor():
    return Color.objects.all()

@register.simple_tag
def gettag():
    return Tag.objects.all()