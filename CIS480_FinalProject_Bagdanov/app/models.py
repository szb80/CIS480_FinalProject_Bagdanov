"""
Definition of models.
"""

from __future__ import unicode_literals
from django.db import models
from django.urls import reverse

from taggit.managers import TaggableManager

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Document(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    department = models.ForeignKey(Department)
    source_file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse('uploadfileapp:home')

    def __str__(self):
        return self.title

#########################################################################################
class CarMake(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name

class Driver(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateField()
    city = models.CharField(max_length=255, help_text="City of Residence", blank=True, null=True)
    car_make = models.ForeignKey(CarMake)
    car_model = models.CharField(max_length=255, help_text="Car model", blank=True, null=True)

    class Meta:
        ordering = ('last_name', 'first_name', )

    def __str__(self):
        return self.last_name + ", " + self.first_name

