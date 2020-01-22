from django.db import models

class Board(models.Model):
    boardNum = models.IntegerField(primary_key=True) #가능하면 surrogate
    nickname = models.CharField(max_length=10, unique=True, null=False)
    title = models.CharField(max_length=15)
    content = models.CharField(max_length=100)
    recommend = models.IntegerField()
    unrecommend = models.IntegerField()
    date = models.DateTimeField()
    category = models.CharField(max_length=10, default="자유")

class Reply(models.Model):
    replyNum = models.IntegerField()
    content = models.CharField(max_length=20, null=False)


# Create your models here.
