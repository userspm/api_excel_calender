from django.db import models

# Create your models here.
class ExcelUpload(models.Model):
    F_name = models.CharField(max_length=50)
    L_name = models.CharField(max_length=20)
    Claim = models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    DOS = models.DateField()
    DOA = models.CharField(max_length=60)
    Appointment_Time = models.CharField(max_length=60)
    Doctor_name = models.CharField(max_length=50)
    Speciality = models.CharField(max_length=50)
    service_type = models.CharField(max_length=50)
    Company = models.CharField(max_length=50)
    Action1 = models.CharField(max_length=50)


    def __str__(self):
        return self.F_name

class FrontDeskModel(models.Model):
    F_name = models.CharField(max_length=50)
    L_name = models.CharField(max_length=20)
    Claim = models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    DOS = models.CharField(max_length=60)
    DOA = models.CharField(max_length=60)
    Doctor_name = models.CharField(max_length=50)
    Company = models.CharField(max_length=50)
    Stage = models.CharField(max_length=100,default='frontdesk')
    active = models.BooleanField(default=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.F_name

class DoctorData(models.Model):
    Doctorname = models.CharField(max_length=50)
    Speciality = models.CharField(max_length=50)
