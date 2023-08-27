from django.db import models


class Employees(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    birthdate = models.DateField()
    email = models.EmailField()
    department = models.ForeignKey('Departments', on_delete=models.SET_NULL, null=True)


class Departments(models.Model):
    department_name = models.CharField(max_length=100)
    floor = models.IntegerField()
    branch = models.ForeignKey('Branches', on_delete=models.CASCADE)


class Branches(models.Model):
    address = models.CharField(max_length=200)
    short_name = models.CharField(max_length=50)
