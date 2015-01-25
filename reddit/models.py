from django.db import models
from django.contrib.auth.models import User

class Subreddit(models.Model):
	name = models.CharField(max_length=50)
	admin = models.ForeignKey(User)

class Post(models.Model):
	creator = models.ForeignKey(User)
	subreddit = models.ForeignKey(Subreddit)
	title = models.CharField(max_length=140)
	nsfw = models.BooleanField(default=False)
	slug = models.SlugField()
	text = models.TextField(blank=True)
	url = models.URLField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

