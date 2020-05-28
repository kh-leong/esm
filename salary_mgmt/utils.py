import urllib.parse

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