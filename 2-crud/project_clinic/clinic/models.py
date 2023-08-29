from django.db import models
from django.utils import timezone


class Patient(models.Model):
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    BirthDate = models.DateField()
    Address = models.CharField(max_length=200)
    Telephone = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)

    class Meta:
        db_table = "Patient"

    def __str__(self):
        return f'''{self.FirstName} {self.LastName}'''


class Doctor(models.Model):
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    BirthDate = models.DateField()
    Address = models.CharField(max_length=200)
    Telephone = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)

    class Meta:
        db_table = "Doctor"

    def __str__(self):
        return f'''{self.FirstName} {self.LastName}'''


class Department(models.Model):
    Name = models.CharField(max_length=200)
    Telephone = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)

    class Meta:
        db_table = "Department"


class Room(models.Model):
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    Number = models.IntegerField()

    class Meta:
        db_table = "Room"


class Appointment(models.Model):
    Patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    Doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    Date = models.DateField()
    Room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "Appointment"


class Prescription(models.Model):
    Appointment = models.ForeignKey(Appointment, on_delete=models.DO_NOTHING)
    StartDate = models.DateField()
    EndDate = models.DateField()
    Medication = models.CharField(max_length=200)
    Approved = models.CharField(max_length=50)

    class Meta:
        db_table = "Prescription"


class Service(models.Model):
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    Price = models.FloatField()

    class Meta:
        db_table = "Service"


class RenderedService(models.Model):
    Appointment = models.ForeignKey(Appointment, on_delete=models.DO_NOTHING)
    Service = models.ForeignKey(Service, on_delete=models.CASCADE)
    Quantity = models.IntegerField()

    class Meta:
        db_table = "RenderedService"


class Invoice(models.Model):
    RenderedService = models.ForeignKey(
        RenderedService, on_delete=models.CASCADE)

    class Meta:
        db_table = "Invoice"


class Job(models.Model):
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    Title = models.CharField(max_length=200)
    StartDate = models.DateField()
    EndDate = models.DateField()

    class Meta:
        db_table = "Job"
