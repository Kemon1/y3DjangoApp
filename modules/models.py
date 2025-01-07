from django.db import models
from django.contrib.auth.models import User, Group
from datetime import date
from courses.models import Course

class Module(models.Model):

    AVAILABILITY_OPTIONS = {
        ('OPEN','Open'),
        ('CLOSED', ('Closed')),
    }

    name = models.CharField(max_length=200, blank=False, null=False)
    code = models.CharField(max_length=200, blank=False, null=False)
    category = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(default=None, blank=True, null=True)
    available = models.CharField(choices=AVAILABILITY_OPTIONS, max_length=200)
    courses = models.ManyToManyField(Course, blank=True)
    

    def str(self):
        return f'{self.name}'
    
