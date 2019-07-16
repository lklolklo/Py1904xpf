from django.contrib import admin
from .models import PollsUser,Foods,Ads
# Register your models here.


class PollUserAdmin(admin.ModelAdmin):
    list_display = {"username"}

class FoodsAdmin(admin.ModelAdmin):
    list_display = {"name"}


admin.site.register(PollsUser)
admin.site.register(Foods)
admin.site.register(Ads)