from django.db import models

# Create your models here.

class BlogEntry(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default='')
	titleMuted = models.CharField(max_length=100, blank=True, default='')
	synopsys = models.TextField(max_length=355)
	teaserImage = models.CharField(max_length=500, blank=False, default='')
	body = models.TextField()
	author = models.ForeignKey('auth.User', related_name='blog')

	class Meta:
		ordering = ('created',) 
