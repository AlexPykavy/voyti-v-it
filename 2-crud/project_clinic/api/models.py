from tastypie.resources import ModelResource
from clinic.models import Patient, Doctor, Appointment, Job, Prescription, Room, Department, RenderedService, Service, Invoice
from tastypie.authorization import Authorization
from .authentication import CustomAuthentication


class PatientResource(ModelResource):
    class Meta:
        queryset = Patient.objects.all()
        resource_name = 'patients'
        allowed_methods = ['get', 'post', 'delete', 'put']
        authentication = CustomAuthentication()
        authorization = Authorization()


class DoctorResource(ModelResource):
    class Meta:
        queryset = Doctor.objects.all()
        resource_name = 'doctors'
        allowed_methods = ['get', 'post', 'delete', 'put']
        authentication = CustomAuthentication()
        authorization = Authorization()


class AppointmentResource(ModelResource):
    class Meta:
        queryset = Appointment.objects.all()
        resource_name = 'appointments'
        allowed_methods = ['get', 'post', 'delete', 'put']
        authentication = CustomAuthentication()
        authorization = Authorization()


class JobResource(ModelResource):
    class Meta:
        queryset = Job.objects.all()
        resource_name = 'jobs'
        allowed_methods = ['get', 'post', 'delete', 'put']
        authentication = CustomAuthentication()
        authorization = Authorization()


class PrescrtiptionResource(ModelResource):
    class Meta:
        queryset = Prescription.objects.all()
        resource_name = 'prescriptions'
        allowed_methods = ['get', 'post', 'delete', 'put']
        authentication = CustomAuthentication()
        authorization = Authorization()


class RoomResource(ModelResource):
    class Meta:
        queryset = Room.objects.all()
        resource_name = 'rooms'
        allowed_methods = ['get', 'post', 'delete', 'put']
        authentication = CustomAuthentication()
        authorization = Authorization()


class DepartmentResource(ModelResource):
    class Meta:
        queryset = Department.objects.all()
        resource_name = 'departments'
        allowed_methods = ['get', 'post', 'delete', 'put']
        authentication = CustomAuthentication()
        authorization = Authorization()


class RenderedServiceResource(ModelResource):
    class Meta:
        queryset = RenderedService.objects.all()
        resource_name = 'rendered_services'
        allowed_methods = ['get', 'post', 'delete', 'put']
        authentication = CustomAuthentication()
        authorization = Authorization()


class InvoiceResourse(ModelResource):
    class Meta:
        queryset = Invoice.objects.all()
        resource_name = 'invoices'
        allowed_methods = ['get', 'post', 'delete', 'put']
        authentication = CustomAuthentication()
        authorization = Authorization()


class ServiceResourse(ModelResource):
    class Meta:
        queryset = Service.objects.all()
        resource_name = 'services'
        allowed_methods = ['get', 'post', 'delete', 'put']
        authentication = CustomAuthentication()
        authorization = Authorization()
