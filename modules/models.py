from django.db import models
from django.contrib.auth.models import User, Group
from datetime import date

class Module(models.Model):

    AVAILABILITY_OPTIONS = {
        ('OPEN','Open'),
        ('CLOSED', ('Closed')),
    }

    name = models.CharField(max_length=200, blank=False, null=False)
    code = models.CharField(max_length=200, blank=False, null=False)
    #category =
    description = models.TextField(default=None, blank=True, null=True)
    available = models.CharField(choices=AVAILABILITY_OPTIONS, max_length=200)
    #courses =
    #enrolled_students = 

    def str(self):
        return f'{self.name}'
    
class Registration(models.Model):

    #student =
    module = models.ManyToManyField(Module ,blank=True)
    registration_date = models.DateField(date.today) 
