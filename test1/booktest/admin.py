from django.contrib import admin
from .models import *


#django自带的强大后台管理
# Register your models here.

class HeroInfoIine(admin.StackedInline):
    model = HeroInfo
    extra = 1


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ["title","pub_date"]
    inlines = [HeroInfoIine]



class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ["name","content"]

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)

