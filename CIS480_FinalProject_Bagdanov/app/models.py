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
    tags = TaggableManager(blank=True)

    def get_absolute_url(self):
        return reverse('uploadfileapp:home')

    def __str__(self):
        return self.title
