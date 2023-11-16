from django.db import models

# Create your models here.

class Student(models.Model):
    Sno = models.IntegerField(null=False,blank=False)
    Sname = models.CharField(max_length=50,null=False, blank=False)
    Sclass = models.IntegerField(null=False,blank=False)
    Saddress = models.CharField(max_length=100,null=False,blank=False)