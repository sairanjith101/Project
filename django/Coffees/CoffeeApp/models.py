from django.db import models
import os
import datetime

# Create your models here.

def getFileName(request,filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename = "%s%s"%(now_time, filename)
    return os.path.join('upload/',new_filename)

class Coffee(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    image = models.ImageField(upload_to=getFileName, null=False, blank=False)

    def __str__(self):
        return self.name