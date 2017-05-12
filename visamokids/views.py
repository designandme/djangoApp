from django.shortcuts import render,render_to_response
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string



# Create the views which we have defined in the urls.py inside the urlpatterns
# i.e. implement(define) the student_detail and index views

from visamokids.models import Student,Donor


def index(request):
	if request.user.is_active:
		students = Student.objects.all()
		donors = Donor.objects.all()
		return render(request,'visamokids/index.html', {
			'students':students,
			'donors':donors,		
		})
	return render(request,'login_page.html',{})
	# sending the students created on line 12 with key as "students" into the index.html


def student(request):
	if request.user.is_active:

		students = Student.objects.all()
		return render(request,'visamokids/student.html', {
			'students':students,
		})
	return render(request,'login_page.html',{})

def donor(request):
	donors = Donor.objects.all()
	return render(request,'visamokids/donor.html', {
			'donors':donors,		
		})		


def student_detail(request, gr_no):
	# return HttpResponse('<p> In Student Detail View. Student id {0} </p>'.format(id))
	# here we are using format method to use String Interpolation
	
	try:
		student = Student.objects.get(gr_no=gr_no)
	except Student.DoesNotExist:
		raise Http404('This Student does not exist!')	
	return render(request, 'visamokids/student_detail.html', {
			'student':student,
		})	


def sendEmail(request, id):

	try:
		donor = Donor.objects.get(id=id)
		to_email = donor.email

		msg_plain = render_to_string('email.txt', {'donor_renewal_date': donor.reminder_date})
		msg_html = render_to_string('email.html', {'donor_renewal_date': donor.reminder_date})

		send_mail(
			'Visamo Kids - Greetings our valued Donor',
			msg_plain,
			'visamokids@calorx.org',
			[to_email],
			html_message=msg_html,
		)
	except Donor.DoesNotExist:
		raise Http404('This Donor does not exist!')
	return render(request, 'visamokids/send_email.html', {
			'donor':donor,
		})



def donor_detail(request, id):
	
	try:
		donor = Donor.objects.get(id=id)
	except Donor.DoesNotExist:
		raise Http404('This Donor does not exist!')	
	return render(request, 'visamokids/donor_detail.html', {
			'donor':donor,
		})

def login_view(request):
	if request.POST:
		username=request.POST['username']
		password=request.POST['password']
		user= authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			return render(request, 'visamokids/index.html', {'username':username})

	return render(request,'login_page.html',{})






