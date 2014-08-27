from django.shortcuts import render
import accounts
from django.contrib.auth.decorators import login_required
# Create your views here.
# @login_required
def landing_page(request):
	# user = request.user
	# employer_object = accounts.models.Employer.objects.get(user=user)
	return render(request, 'static_pages/landing_page.html')
	