from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length = 20)
    pud_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Hero(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=True)
    content = models.CharField(max_length=100)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)

    def __str__(self):
        return self.name