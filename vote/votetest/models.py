from django.db import models

# Create your models here.


#问题类
class Ques(models.Model):
    question = models.CharField(max_length=20)
    option1 = models.CharField(max_length=10,default="None")
    option2 = models.CharField(max_length=10, default="None")
    option3 = models.CharField(max_length=10, default="None")
    option4 = models.CharField(max_length=10, default="None")


#统计类
class Count(models.Model):
    question = models.ForeignKey(Ques,on_delete=models.CASCADE)
    opt1 = models.DecimalField(max_digits=3,decimal_places=0,default=0)
    opt2 = models.DecimalField(max_digits=3, decimal_places=0,default=0)
    opt3 = models.DecimalField(max_digits=3, decimal_places=0,default=0)
    opt4 = models.DecimalField(max_digits=3, decimal_places=0,default=0)