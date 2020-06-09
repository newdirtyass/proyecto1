from django.db import models

class Post(models.Model):
	title = models.TextField()
	author = models.TextField()
	body = models.TextField()

	def __str__(self):
		return self.title + " The author is " + self.author

# Create your models here.
