from django.contrib import admin
from .models import profile
from .models import Shipment
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(profile)
admin.site.register(Shipment)

