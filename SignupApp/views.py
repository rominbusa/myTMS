''' /SignupApp/views.py '''

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from SignupApp.models import TMSUser
from django.contrib.auth.models import User

def signup(request):
    c={}
    c.update(csrf(request))
    return render(request,'signup.html',c)

def adduserinfo(request):
	uname=request.POST.get('username','')
	pwd=request.POST.get('password','')
	cpwd=request.POST.get('cpassword','')
	emailid=request.POST.get('emailid','')
	mno=request.POST.get('mobileno','')
	if(pwd==cpwd):
		if(len(pwd)>8):
			u=User.objects.create_user(username=uname,password=pwd,email=emailid)
			print(u)
			u.TMSUser = TMSUser(user=u,mobileno=mno)
			u.TMSUser.save()
			u.save()
			return HttpResponseRedirect('/loginmodule/login/')
		else:
			return render(request,'signup.html',{"error1":"password length is lessthan 8"})
	else:
		return render(request,'signup.html',{"error2":"password doesn't match enter again"})