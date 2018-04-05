''' /SignupApp/urls.py '''

from SignupApp.views import *
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns=[
	url(r'^signup/',signup),
	url(r'^adduserinfo/',adduserinfo),
]