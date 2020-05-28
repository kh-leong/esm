import urllib.parse
from django.db import transaction
from .models import EmployeeSalary
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def isFloat(salary):
    return salary.replace('.', '', 1).isnumeric()

def isValidSort(sort):
    if len(sort) < 2:
        return False
    
    if sort[0] != '+' and sort[0] != '-':
        return False

    column = sort[1:]
    if column != 'id' and column != 'login' and column != 'name' and column != 'salary':
        return False

    return True

def isSortAscending(sort):
    if sort[0] == '+':
        return True
    return False

def isParamEncoded(param):
    return param != urllib.parse.unquote(param)

def decodeParam(param):
    decoded = urllib.parse.unquote(param)
    return decoded


def handleUploadedCsv(csv):
    data = csv.read().decode('utf-8')
    lines = data.split("\n")
    # ignore first line
    dataLines = lines[1:]
    try:
        with transaction.atomic():
            for line in dataLines:
                # ignore comments
                if line[0] == '#':
                    continue
                # save to db
                rowData = line.split(',')
                if len(rowData) != 4:
                    raise ValueError('Incorrect number of columns')
                csvId = rowData[0]
                csvLogin = rowData[1]
                csvName = rowData[2]
                csvSalary = float(rowData[3])
                if csvSalary <= 0:
                    raise ValueError('Salary cannot be negative')
                # 
                EmployeeSalary.objects.update_or_create(
                    id=csvId, login=csvLogin,
                    defaults = {
                        'id': csvId,
                        'login': csvLogin,
                        'name':csvName,
                        'salary': csvSalary
                    }
                )
    except Exception as e:
        logger.error("Could not save")
        logger.error("Error: " + str(e))
        return False
    return True
