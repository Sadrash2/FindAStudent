from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
import django.contrib.auth
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
import accounts
import tempfile
from django.shortcuts import render_to_response
# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_ qfile
# Create your views here.

def sign_in(request):
	
	if request.POST:
		username = request.POST.get('user')
		password = request.POST.get('pass')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('landing_page'))
		else:
			return render(request, 'static_pages/sign_in.html')
	return render(request, 'static_pages/sign_in.html')

def sign_up(request):

	if request.POST:
		username = request.POST.get('user')
		password = request.POST.get('pass') 
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		industry = request.POST.get('industry')
		reg_no = request.POST.get('reg_no')
		company_name = request.POST.get('company_name')
		designation = request.POST.get('designation')
		email = request.POST.get('email')
		phone_no = request.POST.get('phone_no')
		address = request.POST.get('address')
		company_size = request.POST.get('company_size')
		working_hours = request.POST.get('working_hours')
		dress_code = request.POST.get('dress_code')
		benefits = request.POST.get('benefits')
		transportation = request.POST.get('transportation')
		website = request.POST.get('website')
		social_media_link = request.POST.get('social_media_link')
		company_overview = request.POST.get('company_overview')
		mission = request.POST.get('mission')
		vission = request.POST.get('vission')
		# logo = request.FILES['logo']
		# header = request.FILES['header']
		why_join_us = request.POST.get('why_join_us')

		# try:
		new_account = django.contrib.auth.models.User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password)
		new_account.save()
		user1 = authenticate(username=username, password=password)
	
		if user1 is not None:
			if user1.is_active:

				# if user is valid and user/pass are correct we create the employer login here
				# user1 has the entire object of the user, then = user (django gets the pk of the user1 and puts to there) and if user's logged in user1= request.user
				new_employer = accounts.models.Employer(user=user1, company_name=company_name, industry=industry, 
					company_reg_no=reg_no, contact_person_name=first_name, designation=designation, email=email,
					telephone_no=phone_no, location=address, company_size=company_size, working_hours=working_hours, dress_code=dress_code, benefits=benefits, 
					transportation=transportation, website=website, social_media_link=social_media_link, company_overview=company_overview, mission=mission, vission=vission,
					why_join_us=why_join_us )

				new_employer.save()

				login(request, user1)
				return HttpResponseRedirect(reverse('landing_page'))
		else:
			messages.add_message(request, messages.ERROR, 'Something went wrong! Please retry.')
			return HttpResponseRedirect('/sign_up.html')

		# except:
		# 	messages.add_message(request, messages.ERROR, 'You seem to already have an account with us, try to login first please.')
		# 	return HttpResponseRedirect('/sign_up')

	return render(request, 'static_pages/sign_up.html')

def logout_view(request):
	logout(request)
	return render(request,'static_pages/landing_page.html')
