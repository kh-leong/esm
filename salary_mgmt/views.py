from django.shortcuts import render
from salary_mgmt.models import EmployeeSalary
from django.core import serializers
from django.http import HttpResponse

# Create your views here.
def user_index(request):
    entries = EmployeeSalary.objects.all()
    context = {
        'entries': entries
    }
    return render(request, 'user_index.html', context)

def user_detail(request, primary_key):
    entries = EmployeeSalary.objects.get(pk = primary_key)
    context = {
        'entries': entries
    }
    return render(request, 'user_index.html', context)

def get_user(request):
    entries = EmployeeSalary.objects.all()
    entries_json = serializers.serialize('json', entries)

    return HttpResponse(entries_json, content_type='application/json')