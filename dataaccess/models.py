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

class Review(models.Model):
    username = models.ForeignKey('UserProfile', null=True, on_delete = models.SET_NULL)
    productid = models.ForeignKey('Product', null=True, on_delete = models.SET_NULL)
    rating = models.IntegerField()
    details = models.TextField()

    class Meta:
        unique_together = (("username", "productid"),)

    def __unicode__(self):
        return unicode(str(self.username) + " " + str(self.productid))

class Cart(models.Model):
    username = models.ForeignKey('UserProfile', null=True, on_delete = models.SET_NULL)
    productid = models.ForeignKey('Product', null=True, on_delete = models.SET_NULL)
    count = models.IntegerField()

    class Meta:
        unique_together = (("username", "productid"),)
    
    def __unicode__(self):
        return unicode(str(self.username) + " " + str(self.productid))

class Order(models.Model):
    username = models.ForeignKey('UserProfile', null=True, on_delete = models.SET_NULL)
    productid = models.ForeignKey('Product', null=True, on_delete = models.SET_NULL)
    count = models.IntegerField()
    delivstatus = models.CharField(max_length=10)
    orderid = models.CharField(max_length=30)
    duedate = models.CharField(max_length=30)
    contactno = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    amount = models.FloatField()
    paymentmethod = models.CharField(max_length=30)
    paymentinfo = models.CharField(max_length=30)
    
    def __unicode__(self):
        return unicode(str(self.username) + " " + str(self.productid))

