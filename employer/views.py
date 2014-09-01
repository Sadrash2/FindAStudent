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
	jobs = employer.models.EmployerJob.objects.filter(user=user1)

	if request.POST:
		username = request.POST.get('user')
		title = request.POST.get('title')
		role = request.POST.get('role')
		location = request.POST.get('location')
		responsibilities = request.POST.get('responsibility')
		requirements = request.POST.get('requirements')
		how_to_apply = request.POST.get('how_to_apply')
		salary = request.POST.get('salary')
		post_date = datetime.now()
		deadline = request.POST.get('deadline')
		try:
			user1 = accounts.models.Employer.objects.get(user=user)
			print user1
			new_employer_job = employer.models.EmployerJob(user=user1, title=title, role=role, 
						location=location,responsibilities=responsibilities, requirements=requirements, 
						how_to_apply=how_to_apply, salary=salary, post_date=post_date, deadline=post_date )
			new_employer_job.save()
			messages.add_message(request, messages.ERROR, 'You have successfully posted a new job.')
			return render(request,'employer/post_job.html')
		except:
			messages.add_message(request, messages.ERROR, 'Something went wrong! Please retry.')
			return render(request,'employer/post_job.html')
	return render(request,'employer/post_job.html',{'jobs':jobs,})
