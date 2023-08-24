"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.models import PatientResource, DoctorResource, AppointmentResource, JobResource, RenderedServiceResource, ServiceResourse, PrescrtiptionResource, InvoiceResourse, RoomResource, DepartmentResource
from tastypie.api import Api

api = Api(api_name='v1')
doctor_resource = DoctorResource()
patient_resource = PatientResource()
appointment_resource = AppointmentResource()
job_resource = JobResource()
rendered_service_resource = RenderedServiceResource()
service_resource = ServiceResourse()
prescription_resource = PrescrtiptionResource()
invoice_resource = InvoiceResourse()
room_resource = RoomResource()
department_resource = DepartmentResource()

api.register(doctor_resource)
api.register(patient_resource)
api.register(appointment_resource)
api.register(job_resource)
api.register(rendered_service_resource)
api.register(service_resource)
api.register(prescription_resource)
api.register(invoice_resource)
api.register(room_resource)
api.register(department_resource)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('clinic/', include('clinic.urls')),
    path('api/', include(api.urls))

]
