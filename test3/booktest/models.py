from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=20)
    pud_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class HeroInline(models.Manager):
    def addhero(self,name,gender,content,book):
        hero = Hero()
        hero.name = name
        hero.gender = gender
        hero.content = content
        hero.book = book
        hero.save()


class Hero(models.Model):
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=5,choices=(("man","男"),("women","女")))
    # gender = models.CharField(max_length=5, choices=(("man", "男"), ("women", "女")))
    content = models.CharField(max_length=10)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    objects = HeroInline()


    def __str__(self):
        return self.name