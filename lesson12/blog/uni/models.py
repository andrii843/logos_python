from __future__ import unicode_literals

from django.db import models

# Create your models here.


class University(models.Model):
	name = models.CharField(
		max_length = 50,
	)
	
class ExtraClass(models.Model):
	name = models.CharField(
		max_length = 50,
	)
	
class StudentTicket(models.Model):
	issue_date = models.DateTimeField(
		auto_now_add = True
	)
	numbers = models.IntegerField()
	
class Student(models.Model):
	
	name = models.CharField(
		max_length = 255
	)
	university = models.ForeignKey(
		University,
		on_delete = models.CASCADE
	)
	ticket = models.OneToOneField(
		StudentTicket,
		on_delete = models.CASCADE
	)
	extra_classes = models.ManyToManyField(
		ExtraClass,
		verbose_name='Student extra classes'
	)
	