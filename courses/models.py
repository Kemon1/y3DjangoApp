from django.db import models

class Course(models.Model):

    name = models.CharField(max_length=200, blank=False, null=False)
    code = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(default=None, blank=True, null=True)
    #enrolled_students = 
