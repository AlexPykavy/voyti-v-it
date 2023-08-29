from django.shortcuts import render
from django.http import Http404
from .models import Doctor, Appointment, Job, Patient, Prescription, Invoice, RenderedService, Room, Service, Department
from rest_framework import viewsets
from .serializers import AppointmentSerializer, DoctorSerializer, JobSerializer, PatientSerializer, PrescriptionSerializer, InvoiceSerializer, RenderedServiceSerializer, RoomSerializer, ServiceSerializer, DepartmentSerializer


def index(request):
    doctors = Doctor.objects.all()
    return render(request, 'clinic.html', {'doctors': doctors})


def doctor(request, doctor_id):
    try:
        doctor = Doctor.objects.get(pk=doctor_id)
        return render(request, 'doctor.html', {'doctor': doctor})
    except Doctor.DoesNotExist:
        raise Http404()


class DoctorsViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class AppointmentsViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class JobsViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class PatientsViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PrescriptionsViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer


class InvoicesViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class RenderedServicesViewSet(viewsets.ModelViewSet):
    queryset = RenderedService.objects.all()
    serializer_class = RenderedServiceSerializer


class RoomsViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class DepartmentsViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
