from django.shortcuts import render
from salary_mgmt.models import EmployeeSalary
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, permissions
from salary_mgmt.serializers import EmployeeSalarySerializer
from rest_framework import status
from rest_framework.response import Response

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
    if request.method != "GET":
        return Response(status=status.HTTP_400_BAD_REQUEST)

    minSalary = request.GET.get('minSalary', '')
    # check if minSalary is float.
    if not minSalary.replace('.', '', 1).isnumeric():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    maxSalary = request.GET.get('maxSalary', '')
    # check if maxSalary is float
    if not maxSalary.replace('.', '', 1).isnumeric():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    offset = request.GET.get('offset', '0')
    if not offset.isnumeric():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    offset = int(offset)
    limit = 30

    # sort order columns are id, name, login, salary
    sort = request.GET.get('sort', 'abc')
    if len(sort) <2:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    entries = EmployeeSalary.objects.filter(salary__gte=minSalary)
    entries = entries.filter(salary__lte=maxSalary).order_by('-salary')[offset:offset+limit]
    serializer = EmployeeSalarySerializer(entries, many=True)
    return JsonResponse({'results': serializer.data}, safe=False)
