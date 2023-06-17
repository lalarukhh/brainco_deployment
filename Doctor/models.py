
from django.contrib.auth.models import AbstractUser, Group, Permission # This line is for the login or signup

from django.db import models

# Create your models here.

class Doctors_Prescription(models.Model):
    patient_Id = models.IntegerField(null=True)
    doctor_Id = models.IntegerField(null=True)
    doctor_Name = models.TextField(max_length=100, null=True)
    patient_Name = models.TextField(max_length=100, null=True)
    medicine_Name = models.TextField(max_length=100, null=True)
    medicine_Dossage = models.IntegerField(null=True)
    date = models.DateField(max_length=100, null=True)
    patient_Age = models.IntegerField(null=True)
    tests_To_Done = models.IntegerField(null=True, blank=True)
    date_Of_Birth = models.DateField(null=True, blank=True)
    diagnosed_With = models.TextField(blank=True, null=True)
    suggestions = models.TextField(blank=True, null=True,default="Noo")
    signature = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.doctor_Name
    
class Patient_Record(models.Model):
    patient_Id = models.IntegerField(null=False)
    patient_Name = models.TextField(max_length=100, null=True)
    disease = models.TextField(max_length=100, null=True)
    date = models.DateField(max_length=100, null=True)
    patient_Age = models.IntegerField(null=True)
    suggestions = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    patient_Email=models.EmailField()
    patient_Ph_No = models.IntegerField(default = 0, null=True)

    
    def __str__(self) -> str:
        return self.patient_Name
    

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    specialization = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    email = models.EmailField()
    license_number = models.CharField(max_length=50)

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='customuser_set',
        related_query_name='customuser'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='customuser_set',
        related_query_name='customuser'
    )

    def __str__(self):
        return self.username


