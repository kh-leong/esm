from django.db import models

# Create your models here.
class EmployeeSalary(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    login = models.CharField(max_length=24, unique=True)
    name = models.CharField(max_length=100)
    salary = models.FloatField()

    class Meta:
        ordering = ['id', 'name', 'login', 'salary']