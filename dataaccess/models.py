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