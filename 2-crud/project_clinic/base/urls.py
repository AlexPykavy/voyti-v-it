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

router1 = routers.SimpleRouter()
router1.register(r'appointments', AppointmentsViewSet)

router2 = routers.SimpleRouter()
router2.register(r'doctors', DoctorsViewSet)

router3 = routers.SimpleRouter()
router3.register(r'jobs', JobsViewSet)

router4 = routers.SimpleRouter()
router4.register(r'prescriptions', PrescriptionsViewSet)

router5 = routers.SimpleRouter()
router5.register(r'services', ServicesViewSet)

router6 = routers.SimpleRouter()
router6.register(r'rendered_services', RenderedServicesViewSet)

router7 = routers.SimpleRouter()
router7.register(r'departments', DepartmentsViewSet)

router8 = routers.SimpleRouter()
router8.register(r'invoices', InvoicesViewSet)

router9 = routers.SimpleRouter()
router9.register(r'patients', PatientsViewSet)

router10 = routers.SimpleRouter()
router10.register(r'rooms', RoomsViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('clinic/', include('clinic.urls')),
    path('api/v1/', include(router1.urls)),
    path('api/v1/', include(router2.urls)),
    path('api/v1/', include(router3.urls)),
    path('api/v1/', include(router4.urls)),
    path('api/v1/', include(router5.urls)),
    path('api/v1/', include(router6.urls)),
    path('api/v1/', include(router7.urls)),
    path('api/v1/', include(router8.urls)),
    path('api/v1/', include(router9.urls)),
    path('api/v1/', include(router10.urls))


]
