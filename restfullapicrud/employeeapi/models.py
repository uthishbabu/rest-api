from django.db import models

# Create your models here.

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_codw = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)

# create/insert/add - POST
# retrive / fetch - GET
# Update/ Edit - PUT
# Delet/Remove - DELETE