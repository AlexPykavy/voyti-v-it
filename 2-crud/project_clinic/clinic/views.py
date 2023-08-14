from django.shortcuts import render
from django.http import HttpResponse, Http404 
from .models import Doctor


# Create your views here.
def index(request):
    doctors = Doctor.objects.all()
    return render(request, 'clinic.html', {'doctors': doctors})


def doctor(request, doctor_id):
    try:
        doctor= Doctor.objects.get(pk=doctor_id)
        return render(request, 'doctor.html', {'doctor': doctor} )
    except Doctor.DoesNotExist:
        raise Http404()