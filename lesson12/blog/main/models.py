from django.db import models

# Create your models here.
class Article(models.Model):
	title = models.CharField(
		max_length = 255
	) 
	text = models.TextField()
	created = models.DateTimeField(
		auto_now_add = True
	)
	views = models.IntegerField()
	
	class Meta:
		verbose_name = 'Article'
		verbose_name_plural = 'Articles'