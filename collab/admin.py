from django.contrib import admin
from .models import Devices, DeviceData, DeviceDataVars, Webhook
# Register your models here.
admin.site.register(Devices) # register Devices model
admin.site.register(DeviceData) # register DeviceData model
admin.site.register(DeviceDataVars) # register DeviceDataVars model
admin.site.register(Webhook)