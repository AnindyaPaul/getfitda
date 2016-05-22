from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    picture = models.ImageField(upload_to='ppic', blank=True)
    code = models.CharField(max_length=20)
    verified = models.IntegerField(default='0')
