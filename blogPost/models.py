from django.db import models
from django.contrib import auth
from django.utils import timezone
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
User=get_user_model
# Create your models here.
class User(auth.models.User,auth.models.PermissionsMixin):

	def __str__(self):
		return '@{}'.format(self.username)
	
class blogs(models.Model):
	author=models.ForeignKey(auth.models.User,null=True,blank=True)
	title=models.CharField(max_length=264)
	content=models.TextField()
	create_date=models.DateTimeField(default=timezone.now)
	active=models.BooleanField(default=False)
	description=models.CharField(max_length=264,blank=True)

	def get_absolute_url(self):
		return reverse('thanks')

	def __str__(self):
		return self.title	

	
	 
class comments(models.Model):
	author=models.ForeignKey(auth.models.User,null=True,blank=True)
	blog=models.ForeignKey(blogs)
	content=models.TextField()
	create_date=models.DateTimeField(default=timezone.now)

