from rest_framework import serializers
from salary_mgmt.models import EmployeeSalary

class EmployeeSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeSalary
        fields = ['id', 'login', 'name', 'salary']

