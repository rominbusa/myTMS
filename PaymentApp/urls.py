'''/PaymentApp/urls.py'''

from PaymentApp.views import *
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns=[
	url(r'^CalculateAmount/',CalculateAmount),
	url(r'^makepayment/',makepayment),
	url(r'^bill/',bill),
]