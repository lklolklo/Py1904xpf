from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Question(models.Model):
    desc = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.desc

# class ChoiceManager(models.Manager):
#     def addvote(self,id):
#         c = self.get(pk=1)
#         c.votes += 1
#         c.save()

class Choice(models.Model):
    desc = models.CharField(max_length=20)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    # objects = ChoiceManager()

    def __str__(self):
        return self.desc

class PollsUser(User):
    telephone = models.CharField(max_length=11)