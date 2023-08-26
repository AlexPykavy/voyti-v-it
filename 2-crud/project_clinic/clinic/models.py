from django.db import models
from django.utils import timezone


class Patient(models.Model):
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    BirthDate = models.DateField()
    Telephone = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'''{self.FirstName} {self.LastName}'''


class Doctor(models.Model):
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    BirthDate = models.DateField()
    Telephone = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'''{self.FirstName} {self.LastName}'''


class Department(models.Model):
    Name = models.CharField(max_length=200)
    Telephone = models.CharField(max_length=200)


class Room(models.Model):
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    Number = models.IntegerField()


class Appointment(models.Model):
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Date = models.DateField()
    Room = models.ForeignKey(Room, on_delete=models.CASCADE)


class Prescription(models.Model):
    Appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    StartDate = models.DateField()
    EndDate = models.DateField()
    Medication = models.CharField(max_length=200)
    Approved = models.CharField(max_length=50)


class Service(models.Model):
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    Price = models.FloatField()


class RenderedService(models.Model):
    Appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    Service = models.ForeignKey(Service, on_delete=models.CASCADE)
    Quantity = models.IntegerField()


class Invoice(models.Model):
    RenderedService = models.ForeignKey(
        RenderedService, on_delete=models.CASCADE)


class Job(models.Model):
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    Title = models.CharField(max_length=200)
    StartDate = models.DateField()
    EndDate = models.DateField()
