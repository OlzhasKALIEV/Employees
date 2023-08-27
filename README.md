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

>>> from django.db import models
>>> from faker import Faker
>>> import random
>>> from datetime import date
>>> from company.models import Employees, Departments, Branches
>>> for _ in range(3):
...     address = fake.address()
...     short_name = fake.random_element(['A', 'B', 'C'])
...     branch = Branches.objects.create(address=address, short_name=short_name)
...
...     num_departments = random.randint(2, 5)
...     for _ in range(num_departments):
...         department_name = fake.job()
...         floor = random.randint(1, 5)  # Предположим, у нас 5 этажей в здании
...         department = Departments.objects.create(department_name=department_name, floor=floor, branch=branch)
...
...         num_employees = random.randint(1, 30)
...         for _ in range(num_employees):
...             full_name = fake.name()
...             position = fake.random_element(['Manager', 'Developer', 'Designer', 'Analyst'])  # Предположим, есть только эти должности
...             phone_number = fake.phone_number()
...             birthdate = fake.date_of_birth(minimum_age=18, maximum_age=65)
...             email = fake.email()
...             Employees.objects.create(full_name=full_name, position=position, phone_number=phone_number,
...                                     birthdate=birthdate, email=email, department=department)

>>> count_managers = Employees.objects.filter(position='Manager').count()  
>>> print(count_managers)

>>> for employee in fourth_floor_employees:
...     print(employee)

>>> from django.db.models import Q
>>> branch1_id = 1
>>> branch2_id = 2
>>> employees = Employees.objects.filter(Q(department__branch_id=branch1_id) | Q(department__branch_id=branch2_id))
>>> for employee in employees:
...     print(employee.full_name)


>>> from company.models import Employees, Departments, Branches
>>> branch1_id = 1
>>> branch2_id = 2
>>> employees = Employees.objects.filter(department__branch_id__in=[branch1_id, branch2_id])
>>> for employee in employees:
...     print(employee.full_name)


>>> employees = Employees.objects.exclude(email__isnull=False)
>>> for employee in employees:
...     print(employee.full_name)

>>> from company.models import Employees
>>> import datetime
>>> start_date = datetime.date(1990, 1, 1)
>>> end_date = datetime.date(1990, 12, 31)
>>> employees = Employees.objects.filter(birthdate__range=[start_date, end_date])
>>> for employee in employees:
...     print(employee.full_name)