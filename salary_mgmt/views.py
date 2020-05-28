from django.shortcuts import render
from salary_mgmt.models import EmployeeSalary
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, permissions
from salary_mgmt.serializers import EmployeeSalarySerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from .utils import *

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

@api_view(['GET',])
def get_user(request):
    if request.method != "GET":
        return HttpResponse(status=400)

    minSalary = request.GET.get('minSalary', '')
    # check if minSalary is float.
    if not isFloat(minSalary):
        return HttpResponse(status=400)

    maxSalary = request.GET.get('maxSalary', '')
    # check if maxSalary is float
    if not isFloat(maxSalary):
        return HttpResponse(status=400)

    offset = request.GET.get('offset', '0')
    if not offset.isnumeric():
        return HttpResponse(status=400)
    offset = int(offset)
    limit = 30

    # sort order columns are id, name, login, salary
    sort = request.GET.get('sort', '+salary')
    if isParamEncoded(sort):
        sort = decodeParam(sort)
    if not isValidSort(sort):
        return HttpResponse(status=400)

    entries = EmployeeSalary.objects.filter(salary__gte=minSalary)
    entries = entries.filter(salary__lte=maxSalary)
    if not isSortAscending(sort):
        entries = entries.order_by(sort)
    entries = entries[offset:offset+limit]
    serializer = EmployeeSalarySerializer(entries, many=True)
    return JsonResponse({'results': serializer.data}, safe=False)
