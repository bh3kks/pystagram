# coding: utf-8
from django.db import models
from django.conf import settings

# Create your models here.

class UserProfile(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	profile_image = models.ImageField(upload_to='profile_img')
	description = models.CharField(max_length=300, blank=True)
	