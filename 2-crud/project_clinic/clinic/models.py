from django.db import models
from django.utils import timezone


class Patient(models.Model):
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    BirthDate = models.DateTimeField()
    Telephone = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'''{self.FirstName} {self.LastName}'''


class Doctor(models.Model):
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    BirthDate = models.DateTimeField()
    Telephone = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'''{self.FirstName} {self.LastName}'''
