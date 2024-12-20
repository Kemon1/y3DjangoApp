from django.db import models
from datetime import date

class Student(models.Model):

    name = models.CharField(max_length=200, blank=False, null=False)
    date_of_birth = models.DateField(default=date.today)
    city = models.CharField(max_length=200, blank=False, null=False)
    country = models.CharField(max_length=200, blank=False)
    photo = models.ImageField(default='profile_pics/default.png', upload_to='profile_pics')
