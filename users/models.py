from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_list_or_404

#class Profile(models.Model):

    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    #image = models.ImageField(default='profile_pics/default.png', upload_to='profile_pics')

    #def __str__(self):
        #return f'{self.user.first_name} {self.user.last_name}'

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(default='profile_pics/default_ZX96haY.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}'
    
# def student_profile(sender, instance, created, **kwargs):
#     if created:
#         user_Student = Student(user=instance)
#         user_Student.save()

#         return user_Student
    
# post_save.connect(student_profile, sender=User)