from django.db import models
import django.conf
import django.contrib.auth
import django.contrib.auth.models
# Create your models here.
class Student(django.db.models.Model): 
    user = django.db.models.ForeignKey(django.contrib.auth.models.User)
    userid = django.db.models.PositiveIntegerField(default=1)
    
class Employer(django.db.models.Model):

	To = 'to'
	IT = 'IT'
	choices = (
	    (IT, 'IT'),
	    (To, 'To'),
	)

	user = django.db.models.ForeignKey(django.contrib.auth.models.User)
	employer_id = django.db.models.AutoField(primary_key=True)
	company_name = django.db.models.CharField(max_length=255)
	industry = models.CharField(max_length=255)
	company_reg_no = django.db.models.CharField(max_length=255)
	contact_person_name = django.db.models.CharField(max_length=255)
	designation = django.db.models.CharField(max_length=255)
	email = django.db.models.EmailField(max_length=255)
	telephone_no = django.db.models.CharField(max_length=255)
	location = django.db.models.CharField(max_length=255)
	company_size = django.db.models.CharField(max_length=255, blank = True, null=True)
	working_hours = django.db.models.CharField(max_length=255, blank = True, null=True)
	dress_code = django.db.models.CharField(max_length=255, blank = True, null=True)
	benefits = django.db.models.CharField(max_length=255, blank = True, null=True)
	transportation = django.db.models.CharField(max_length=255, blank = True, null=True)
	website = django.db.models.CharField(max_length=255)
	social_media_link = django.db.models.CharField(max_length=255, blank = True, null=True)
	company_overview = django.db.models.CharField(max_length=255, blank = True, null=True)
	mission = django.db.models.CharField(max_length=255, blank = True, null=True)
	vission = django.db.models.CharField(max_length=255, blank = True, null=True)
	logo = django.db.models.ImageField(upload_to='static_files/images/', blank = True, null=True)
	header = django.db.models.ImageField(upload_to='static_files/images/', blank = True, null=True)
	why_join_us = django.db.models.CharField(max_length=255, blank = True, null=True)
