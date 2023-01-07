from django.db import models
from django.contrib.auth.models import User
from Resources.models import *


Gender = (
			('Male', 'Male'),
			('Female', 'Female'),

			)


Level = (
			('100', '100'),
			('200', '200'),
			('300', '300'),
            ('400', '400'),
            ('500', '500'),

			)
class Student(models.Model):
    User=models.ForeignKey(User, on_delete= models.SET_NULL,blank=True, null=True,)
    profileimage = models.ImageField(upload_to='assets', blank=True)
    FirstName =models.CharField(max_length=300, blank=True, null=True)
    LastName =models.CharField(max_length=300, blank=True, null=True)
    Gender=models.CharField(max_length=200, null=True, choices=Gender , blank=False)
    department =models.ForeignKey(department, on_delete= models.SET_NULL,blank=True, null=True,)
    Level =models.CharField(max_length=300, null=True, choices=Level , blank=False)
    
    def __str__(self):
        return str(self.FirstName)

    @property    
    def imageURL(self):
        try:
            url= self.thumbnail.url
        except:
            url=''
        return url(self)