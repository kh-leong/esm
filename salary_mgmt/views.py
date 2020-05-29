from django.shortcuts import render
from salary_mgmt.models import EmployeeSalary
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from salary_mgmt.serializers import EmployeeSalarySerializer
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from .utils import *
import logging
from django.views.decorators.csrf import csrf_protect
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.
def user_index(request):
    context = {}
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

    # filter salary >= minSalary
    entries = EmployeeSalary.objects.filter(salary__gte=minSalary)
    # filter salary <= maxSalary
    entries = entries.filter(salary__lte=maxSalary)
    # sort by descending
    if not isSortAscending(sort):
        entries = entries.order_by(sort)
    
    count = entries.count()
    pages = int(count/30)
    if (count-offset) % 30 > 0:
        pages += 1
    entries = entries[offset:offset+limit]
    serializer = EmployeeSalarySerializer(entries, many=True)
    page_range = list(range(1, pages+1))
    current_page = int(offset/limit)+1
    if current_page > pages:
        current_page = pages
    return JsonResponse(
        {
            'results': serializer.data,
            'count': count,
            'pages': pages,
            'current_page': current_page,
            'page_range': page_range,
        }, safe=False)


@csrf_protect
def upload_csv(request):
    if request.method != 'POST':
        return HttpResponse(status=400)
    try:
        csv = request.FILES['file']
        if not csv.name.endswith('.csv'):
            return HttpResponse('File is not csv', status=400)

        success = handleUploadedCsv(csv)
        if not success:
            return HttpResponse('Could not update DB', status=400)
        
        return HttpResponse(status=200)
    except Exception as e:
        logger.error('Unable to upload file.')
        logger.error(print(e))
        return HttpResponse(status=400)
