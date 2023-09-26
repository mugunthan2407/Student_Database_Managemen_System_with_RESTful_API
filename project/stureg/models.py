from django.db import models
from phone_field import PhoneField

# Create your models here.
class Stureg(models.Model):
    sname = models.CharField(max_length=100,blank=True)
    srollno = models.CharField(max_length=20,blank=True)
    sdob = models.DateField(blank=True)
    sbg = models.CharField(max_length=20,blank=True)
    pgname = models.CharField(max_length=100,blank=True)
    pgphno = PhoneField(blank=True)
    pgmail = models.EmailField(max_length=100,blank=True)
