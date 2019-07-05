from django.db import models

# Create your models here.


class Question(models.Model):
    desc = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.desc

class Choice(models.Model):
    desc = models.CharField(max_length=20)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        return self.desc