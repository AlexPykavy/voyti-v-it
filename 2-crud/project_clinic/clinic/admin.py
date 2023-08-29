from django.contrib import admin
from . import models

admin.site.register(models.Patient)
admin.site.register(models.Doctor)
admin.site.register(models.Appointment)
admin.site.register(models.Prescription)
admin.site.register(models.Room)
admin.site.register(models.RenderedService)
admin.site.register(models.Invoice)
admin.site.register(models.Department)
admin.site.register(models.Service)
admin.site.register(models.Job)
