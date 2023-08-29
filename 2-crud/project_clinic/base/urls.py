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
from clinic.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'appointment', AppointmentsViewSet)
router.register(r'doctor', DoctorsViewSet)
router.register(r'job', JobsViewSet)
router.register(r'prescription', PrescriptionsViewSet)
router.register(r'service', ServicesViewSet)
router.register(r'rendered_service', RenderedServicesViewSet)
router.register(r'department', DepartmentsViewSet)
router.register(r'invoice', InvoicesViewSet)
router.register(r'patient', PatientsViewSet)
router.register(r'room', RoomsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clinic/', include('clinic.urls')),
    path('api/v1/', include(router.urls)),

]
