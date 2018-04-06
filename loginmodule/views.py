''' /loginmodule/views.py '''

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from BookTicketApp.models import PackageDetails

def home(request):
	c={}
	c.update(csrf(request))
	request.session['temp'] = "xyz"
	c['packs'] = PackageDetails.objects.all()
	return render(request,'home.html',c)

def login(request):
		c={}
		c.update(csrf(request))
		return render(request,'login.html',c)

def auth_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate(username=username, password=password)
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/BookTicketApp/book_ticket/')
	else:
		return render(request,'login.html',{"error":"Username or Password Invalid"})

def logout(request):
	auth.logout(request)
	return render(request, 'logout.html')

def aboutus(request):
	request.session['temp'] = "xyz"
	return render(request,'aboutus.html')
