from __future__ import unicode_literals

from django.db import models

class User(models.Model):
	name = models.CharField(
		max_length=255
	)
	surname = models.CharField(
		max_length=255
	)
	register_date = models.DateField()
	birth_date = models.DateField()
	email = models.EmailField()
	average_mark = models.DecimalField(
		max_digits=3,
		decimal_places=2
	)
	num_studies = models.IntegerField()
	description_about = models.TextField()
	fb_link = models.URLField
	avatar = models.ImageField(
		upload_to='avatars'
	)
	resume = models.FileField(
		upload_to='resumes',
		null=True
	)
	

class Sample(models.Model):
	
	name = models.CharField(
		max_length = 255,
		
		verbose_name = 'User name', 
		help_text = 'Some description'
	)
	start_education = models.DateField(
		auto_now=True
	)
	start_education_time = models.DateTimeField(
		auto_now_add=True
	)
	is_flag = models.BooleanField(
		verbose_name='True or false'
	)
	email = models.EmailField(
		verbose_name='Email'
	)
	
	int_some = models.IntegerField()
	float_some = models.FloatField()
	decimal_some = models.DecimalField(
		max_digits=5,
		decimal_places=3
	)
	
	some_url = models.URLField(
		verbose_name = 'Url address'
	)
	
	some_slug = models.SlugField()
	
	text = models.TextField()
	
	some_file = models.FileField(
		upload_to='samlpes_txt'
	)
	
	some_image = models.ImageField(
		upload_to='img'
	)
	