from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Doctors_Prescription)
admin.site.register(Patient_Record)
admin.site.register(CustomUser)
