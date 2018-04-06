''' /SignupApp/urls.py '''

from SignupApp.views import *
from django.conf.urls import url

urlpatterns=[
	url(r'^signup/',signup),
	url(r'^adduserinfo/',adduserinfo),
]