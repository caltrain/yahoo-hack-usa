from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

class UserAlbums(models.Model):
	user = models.ForeignKey("User")
	album = models.ForeignKey("Albums")

class Albums(models.Model):
	name = models.CharField(max_length=200)
	source_id = models.CharField(max_length=200)
	primary_owner = models.CharField(max_length=200)

class Sources(models.Model):
	album = models.ForeignKey(Albums)
	source_type = models.CharField(max_length=200)
	active = models.CharField(max_length=200)
	link = models.CharField(max_length=200)
