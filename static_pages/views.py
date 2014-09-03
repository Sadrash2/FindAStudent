from django.shortcuts import render
import accounts
import employer
from django.contrib.auth.decorators import login_required
# Create your views here.
# @login_required
def landing_page(request):
	user = request.user
	jobs = employer.models.EmployerJob.objects.all()
	print jobs
	return render(request, 'static_pages/landing_page.html',{'jobs':jobs,})
	