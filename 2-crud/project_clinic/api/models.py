from tastypie.resources import ModelResource
from clinic.models import Patient, Doctor
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
