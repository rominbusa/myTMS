''' /BookTicketApp/urls.py '''

from BookTicketApp.views import *
from django.conf.urls import url

urlpatterns=[
	url(r'^book_ticket/',book_ticket),
	url(r'^bookingdataadd/',bookingdataadd),
	url(r'^booking_history/', booking_history),
	url(r'^delete/',delete),
	url(r'^feedback/',feedback),

]