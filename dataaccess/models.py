from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    picture = models.CharField(max_length=50)
    code = models.CharField(max_length=20)
    verified = models.IntegerField(default='0')

    def __unicode__(self):
        return self.username
    
class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    details = models.TextField()
    
    def __unicode__(self):
        return self.name

class Product(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    price = models.FloatField()
    count = models.IntegerField()
    discount = models.FloatField()
    details = models.TextField()
    sold = models.IntegerField()
    image = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name