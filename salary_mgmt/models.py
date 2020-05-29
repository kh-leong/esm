from django.db import models

# Create your models here.
class EmployeeSalary(models.Model):
    # assumption: id has maximum length of 24
    id = models.CharField(primary_key=True, max_length=24)
    # assumption: login has maximum length of 24
    login = models.CharField(max_length=24, unique=True)
    # assumption: name has maximum length of 100
    name = models.CharField(max_length=100)
    salary = models.FloatField()

    class Meta:
        ordering = ['id', 'name', 'login', 'salary']
