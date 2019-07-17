from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class PollsUser(User):
    telephone = models.CharField(max_length=11,blank=True,null=True)

    def __str__(self):
        return self.username

class Tag(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title

class Color(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title

class Foods(models.Model):
    name = models.CharField(max_length=20)
    price1 = models.IntegerField(default=0)
    price2 = models.IntegerField(default=0)
    # tag  = models.ManyToManyField(Tag)
    tags = models.ManyToManyField(Tag)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    intro = models.CharField(max_length=50)#简介
    shoperintro = models.CharField(max_length=50)#商家介绍
    exintro = models.CharField(max_length=50)#专家评价
    img1 = models.ImageField(upload_to="img")
    img2 = models.ImageField(upload_to="img")
    img3 = models.ImageField(upload_to="img")

    def __str__(self):
        return self.name

