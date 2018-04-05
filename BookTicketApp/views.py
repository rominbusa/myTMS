''' /BookTicketApp/views.py '''

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from BookTicketApp.models import TMSBooking,PackageDetails,feedback
from SignupApp.models import TMSUser
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils.crypto import get_random_string
from django.utils.timezone import datetime


@login_required
def book_ticket(request):
	c={}
	c.update(csrf(request))
	request.session['temp']="xyz"
	request.session['full_name']=request.user.username
	c['packs'] = PackageDetails.objects.all()
	c['randomid']=get_random_string(length=6)

	return render(request,'book_ticket.html',c)

@login_required
def bookingdataadd(request):
	bookingid=request.POST.get('bookingid','')
	from1=request.POST.get('from1','')
	to=request.POST.get('to','')
	package1=request.POST.get('package','')
	date=request.POST.get('date','')
	no_of_person=request.POST.get('person','')
	#print(date)
	s=TMSBooking(booking_id=bookingid,source=from1,destination=to,package=PackageDetails.objects.get(pname=package1),departure_date=date,no_of_person=no_of_person,tmsuser=TMSUser.objects.get(user=request.user))
	if(from1!=to):
		s.save()
		request.session['attr1']=package1
		request.session['nop'] = no_of_person
		request.session['source']=from1
		request.session['destination']=to
		request.session['date']=date
		return HttpResponseRedirect('/PaymentApp/CalculateAmount/')
	else:
		request.session['error3']="Source and Destination can't be same"
		return HttpResponseRedirect('/BookTicketApp/book_ticket/')


def booking_history(request):
	request.session['temp']="abc"
	c={}
	c['today']=datetime.today().date()
	c['bookings'] = TMSBooking.objects.filter(tmsuser=request.user.tmsuser)
	return render(request,'booking_history.html',c)

def delete(request):
	TMSBooking.objects.filter(booking_id=request.POST.get('cancel')).delete()
	return HttpResponseRedirect('/BookTicketApp/booking_history/')

def feedback(request):
	return render(request,'feedback.html')

def addfeedback(request):
	feedback=request.POST.get('feedback','')
	f=feedback(tmsuser=TMSUser.objects.get(user=request.user),feedback=feedback)
	f.save()
	return render(request,'home.html')