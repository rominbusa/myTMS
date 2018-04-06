''' /BookTicketApp/models.py '''

from django.db import models
from SignupApp.models import TMSUser

class PackageDetails(models.Model):
	pname = models.CharField(max_length=20,primary_key=True)
	amount = models.CharField(max_length=5)

class TMSBooking(models.Model):
	booking_id=models.CharField(max_length=6,primary_key=True)
	tmsuser = models.ForeignKey(TMSUser,on_delete=models.CASCADE,null=True)
	source = models.CharField(max_length=20)
	destination = models.CharField(max_length=20)
	package = models.ForeignKey(PackageDetails,on_delete=models.CASCADE,null=True)
	departure_date = models.DateField()
	no_of_person = models.PositiveIntegerField(default=0)
	amount=models.PositiveIntegerField()

class feedback(models.Model):
	tmsuser = models.ForeignKey(TMSUser, on_delete=models.CASCADE, null=True)
	feedback=models.TextField(max_length=200)
