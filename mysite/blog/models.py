from django.db import models
from django.core.urlresolvers import reverse


class Post(models.Model):
	title = models.CharField(max_length=140)
	body = models.TextField(max_length=500)
	date = models.DateTimeField(auto_now_add = True, auto_now = False)
	
	def get_absolute_url(self):
		return reverse('blog')
	
	def __str__(self):
		return self.title