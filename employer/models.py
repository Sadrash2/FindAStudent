from django.db import models
import django.conf
import django.contrib.auth
import accounts
import django.contrib.auth.models
import accounts
# Create your models here.
class EmployerJob(django.db.models.Model): 
	user = django.db.models.ForeignKey(accounts.models.Employer)
	title = django.db.models.CharField(max_length=255)
	role = django.db.models.CharField(max_length=255)
	location = django.db.models.CharField(max_length=255)
	responsibilities = django.db.models.CharField(max_length=255)
	requirements = django.db.models.CharField(max_length=255)
	how_to_apply = django.db.models.CharField(max_length=255)
	salary = django.db.models.CharField(max_length=255)
	post_date = django.db.models.DateTimeField(max_length=255)
	deadline = django.db.models.DateTimeField(max_length=255)

	# def save(self, *args, **kwargs):
	# 	title['title']
	# 	super(EmployerJob, self).save(*args, **kwargs)
	# 	