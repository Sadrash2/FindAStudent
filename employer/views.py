from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
import employer
import accounts
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def post_job(request):

	user = request.user
	user1 = accounts.models.Employer.objects.get(user=user)

	if request.POST:
		title = request.POST.get('title')
		role = request.POST.get('role')
		location = request.POST.get('location')
		responsibilities = request.POST.get('responsibility')
		requirements = request.POST.get('requirements')
		how_to_apply = request.POST.get('how_to_apply')
		salary = request.POST.get('salary')
		post_date = datetime.now()
		deadline = request.POST.get('deadline')
		print title, role,location,responsibilities,requirements, how_to_apply, salary, post_date, deadline
		# try:
		new_employer_job = employer.models.EmployerJob(user=user1, title=title, role=role, 
					location=location,responsibilities=responsibilities, requirements=requirements, 
					how_to_apply=how_to_apply, salary=salary, post_date=post_date, deadline=post_date)
		new_employer_job.save()
		messages.add_message(request, messages.ERROR, 'You have successfully posted a new job.')
		return render(request,'employer/post_job.html')
		# except:
		# 	messages.add_message(request, messages.ERROR, 'Something went wrong! Please retry.')
		# 	return render(request,'employer/post_job.html')
	return render(request,'employer/post_job.html')

@login_required
def manage_jobs(request):

	user = request.user
	user1 = accounts.models.Employer.objects.get(user=user)
	jobs = employer.models.EmployerJob.objects.filter(user=user1)

	# if request.POST:
	# 	job_id = request.POST.get('id')
		# delete this job, needs to have js handling that

	return render(request,'employer/manage_jobs.html',{'jobs':jobs,})

@login_required
def employer_profile(request):
	user = request.user
	employers_profile = accounts.models.Employer.objects.get(user=user)
	user1 = accounts.models.Employer.objects.get(user=user)
	if request.POST:
		industry = request.POST.get('industry')
		reg_no = request.POST.get('reg_no')
		contact_name = request.POST.get('contact_name') 
		designation = request.POST.get('designation')
		email = request.POST.get('email')
		phone_no = request.POST.get('phone_no')
		location = request.POST.get('location')
		company_size = request.POST.get('company_size')
		working_hours = request.POST.get('working_hours')
		dress_code = request.POST.get('dress_code')
		benefits = request.POST.get('benefits')
		website = request.POST.get('website')
		transportation = request.POST.get('transportation')
		social_media = request.POST.get('social_media')
		company_overview = request.POST.get('company_overview')
		mission = request.POST.get('mission')
		vission = request.POST.get('vission')
		why_join_us = request.POST.get('why_join_us')
		try:
			accounts.models.Employer.objects.filter(user=user).update(industry=industry, 
						company_reg_no=reg_no, contact_person_name=contact_name, designation=designation, email=email,
						telephone_no=phone_no, location=location, company_size=company_size, working_hours=working_hours, dress_code=dress_code, benefits=benefits, 
						transportation=transportation, website=website, social_media_link=social_media, company_overview=company_overview, mission=mission, vission=vission,
						why_join_us=why_join_us)
			messages.add_message(request, messages.SUCCESS, 'You have successfully updated your changes')
			return render(request,'employer/employer_profile.html',{'employers_profile':employers_profile,})
		except:
			messages.add_message(request, messages.ERROR, 'Something went wrong, Please retry')
			return render(request,'employer/employer_profile.html')

		
	return render(request,'employer/employer_profile.html',{'employers_profile':employers_profile,})








