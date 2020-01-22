from django.db import models

# Create your models here.

class UserInfo(models.Model):
    identifier = models.CharField(max_length=10, primary_key=True)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.identifier