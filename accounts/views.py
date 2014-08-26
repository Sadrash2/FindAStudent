from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
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
	return render(request, 'static_pages/sign_up.html')

def logout_view(request):
	logout(request)
	return render(request,'static_pages/landing_page.html')

	