''' /loginmodule/urls.py '''

from loginmodule.views import *
#from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns=[
    url(r'^home/',home),
    url(r'^login/',login),
    url(r'^logout/',logout),
    url(r'^auth/',auth_view),
    url(r'^aboutus/',aboutus),
]