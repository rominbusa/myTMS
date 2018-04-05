''' myTMS/urls.py(project's urls.py) '''

from django.contrib import admin
from django.conf.urls import url,include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^loginmodule/', include('loginmodule.urls')),
    url(r'^SignupApp/', include('SignupApp.urls')),
    url(r'^BookTicketApp/', include('BookTicketApp.urls')),
    url(r'^PaymentApp/', include('PaymentApp.urls')),
]
