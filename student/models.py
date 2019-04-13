from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Student(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    name = models.CharField(max_length=100,blank=True,null=True)
    mentor = models.CharField(max_length=100,default='sejal thakkar',blank=True,null=True)
    number = models.IntegerField(blank=True,null=True,default=8154057515)
    father = models.IntegerField(blank=True,null=True,default=8140516739)
    mother = models.IntegerField(blank=True,null=True,default=7984426396)

    def __str__(self):
        return self.id


# class Attendance(models.Model):
#     id = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
#
#     def __str__(self):
#         return self.id

