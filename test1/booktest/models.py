from django.db import models
#mvt 中的m 数据模型 用于和数据库交互
#orm对象
# Create your models here.

class BookInfo(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Hero(models.Manager):
    def addhero(self,_name,_content,_gender,_book):
        hero = HeroInfo()
        hero.name = _name
        hero.content = _content
        hero.gender = _gender
        hero.book = _book
        hero.save()

class HeroInfo(models.Model):
    name = models.CharField(max_length=20)
    # gender = models.BooleanField(default=True)
    gender = models.CharField(max_length=5,choices=(("man","男"),("women","女"))  )
    content = models.CharField(max_length=100)
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    objects = Hero()


    def __str__(self):
        return self.name