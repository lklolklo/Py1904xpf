from django.contrib import admin
from .models import Question,Choice
# Register your models here.

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1


class QuestionsAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


admin.site.register(Question,QuestionsAdmin)
admin.site.register(Choice)