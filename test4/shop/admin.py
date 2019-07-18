from django.contrib import admin
from .models import *
# Register your models here.


class PollUserAdmin(admin.ModelAdmin):
    list_display = {"username"}

class FoodsAdmin(admin.ModelAdmin):
    list_display = {"name"}

class TagAdmin(admin.ModelAdmin):
    list_display = {"title"}

class ColorAdmin(admin.ModelAdmin):
    list_display = {"title"}



admin.site.register(PollsUser)
admin.site.register(Tag)
admin.site.register(Color)
admin.site.register(Foods)
admin.site.register(Cart)
