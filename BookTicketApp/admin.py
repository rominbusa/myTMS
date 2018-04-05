''' /BookTicketApp/admin.py '''

from django.contrib import admin
from .models import PackageDetails

admin.site.register(PackageDetails)