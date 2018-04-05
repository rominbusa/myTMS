''' /SignupApp/models.py '''

from django.db import models
from django.contrib.auth.models import User

class TMSUser(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	mobileno = models.CharField(max_length=10)
