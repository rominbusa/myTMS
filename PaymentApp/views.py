''' /PaymentApp/views.py '''

from django.shortcuts import render
from django.template.context_processors import csrf
from BookTicketApp.models import PackageDetails,TMSBooking
from django.contrib.auth.decorators import login_required
from SignupApp.models import TMSUser
from .models import TMSPayment
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.http import HttpResponseRedirect
from django.utils.crypto import get_random_string

@login_required
def CalculateAmount(request):
    pack = request.session.get('attr1')
    nop=request.session.get('nop')
    c = {}
    amt=PackageDetails.objects.get(pname=pack).amount
    request.session['total_amount']=int(amt)*int(nop)
    c['bookings'] = TMSBooking.objects.filter(tmsuser=request.user.tmsuser)
    return render(request,'amount.html',c)

@login_required
def makepayment(request):
    c={}
    c.update(csrf(request))
    request.session['mode']=request.POST.get('mode','')
    return render(request,'payment_mode.html',c)

@login_required
def bill(request):
    c={}
    paymentid=get_random_string(length=6)
    mode=request.session.get('mode')
    amount=request.session.get('total_amount')
    p=TMSPayment(payment_id=paymentid,amount=amount,mode=mode,tmsuser=TMSUser.objects.get(user=request.user))
    p.save()
    return render(request,'bill.html',c)