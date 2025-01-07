from django.db import models
from modules.models import Module
from users.models import Student
from datetime import date


class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=False, null=False)
    module = models.ForeignKey(Module ,on_delete=models.CASCADE, blank=False, null=False)
    registration_date = models.DateField(date.today) 

    class Meta:
        unique_together = ('student', 'module')

    def __str__(self):
        return f'{self.student}{self.module.name}'
