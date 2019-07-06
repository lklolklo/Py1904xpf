from django.contrib import admin
from .models import *
# Register your models here.


class HeroInline(admin.StackedInline):
    model = Hero
    extra = 1


class BookAdmin(admin.ModelAdmin):
    list_display = ["title","pud_date"]
    inlines = [HeroInline]

class HeroAdmin(admin.ModelAdmin):
    list_display = ["name","content"]

admin.site.register(Book,BookAdmin)
admin.site.register(Hero,HeroAdmin)
