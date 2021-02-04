import re
import json
import string
import uuid
import requests
import numpy as np
from sympy import *
from datetime import datetime
from multiprocessing import Value

COUNTER = Value("i", 0)


def getIPAddress():
    return requests.get('https://api.ipify.org').text


def getMACAddress():
    return ':'.join(re.findall('..', '%012x' % uuid.getnode()))


def getFunctionResult(function, vargs, **flags):
    numbers = vargs.split("/")
    try:
        if not flags:
            result = function(numbers)
        else:
            if function is sortNumbers:
                result = function(numbers, reverse=flags["reverse"])
        result = json.dumps(result)
        return result, 200
    except Exception as e:
        print(str(e))   # should I return this?
        return f"Bad request: {e}", 400  # should I also call home page?


def addition(numbers):
    result = float(numbers[0])
    for num in numbers[1:]:
        result += float(num)
    return result


def subtraction(numbers):
    result = float(numbers[0])
    for num in numbers[1:]:
        result -= float(num)
    return result


def multiplication(numbers):
    result = float(numbers[0])
    for num in numbers[1:]:
        result *= float(num)
    return result


def division(numbers):
    result = float(numbers[0])
    for num in numbers[1:]:
        result /= float(num)
    return result


def sine(numbers):
    result = list()
    for num in numbers:
        result.append(np.sin(float(num)))

    if len(result) == 1:
        return result[0]
    else:
        return result


def cosine(numbers):
    result = list()
    for num in numbers:
        result.append(np.cos(float(num)))

    if len(result) == 1:
        return result[0]
    else:
        return result


def tangent(numbers):
    result = list()
    for num in numbers:
        result.append(np.tan(float(num)))

    if len(result) == 1:
        return result[0]
    else:
        return result


def factorialNumber(numbers):
    result = list()
    for num in numbers:
        result.append(np.factorial(int(num)))

    if len(result) == 1:
        return result[0]
    else:
        return result


def sortNumbers(numbers, reverse=False):
    numbers = list(map(float, numbers))
    result = sorted(numbers, reverse=reverse)
    return result


def sortNumbersIncreasing(numbers):
    result = sortNumbers(numbers)
    return result


def sortNumbersDecreasing(numbers):
    result = sortNumbers(numbers, reverse=True)
    return result


def getMatrices(numbers):  # url/nmatrices/ndims/dim1/.../dimn/num1...
    numbers = list(map(float, numbers))
    nmatrices = int(numbers[0])
    ndims = int(numbers[1])
    dims = [int(numbers[i]) for i in range(2, 2+ndims)]
    matrix_values = np.split(np.asarray(numbers[2+ndims:]), nmatrices)
    matrices = [np.reshape(m, dims).tolist() for m in matrix_values]

    if nmatrices == 1:
        return matrices[0]
    else:
        return matrices


def addMatrices(numbers):
    matrices = getMatrices(numbers)
    result = np.add(*matrices).tolist()
    return result


def subtractMatrices(numbers):
    matrices = getMatrices(numbers)
    result = np.subtract(*matrices).tolist()
    return result


# url/exp/e/b1/b2/b3/.../bk
def exponent(numbers):
    e = float(numbers[0])
    bases = numbers[1:]
    result = list()
    for b in bases:
        result.append(float(b)**e)

    if len(result) == 1:
        return result[0]
    else:
        return result

# url/log/b/n1/n2/n3/../nk


def logarithm(numbers):
    base = float(numbers[0])
    nums = numbers[1:]
    result = list()
    for n in nums:
        result.append(np.log10(float(n))/np.log10(base))

    if len(result) == 1:
        return result[0]
    else:
        return result


def natural_log(numbers):
    result = list()
    for num in numbers:
        result.append(np.log(float(num)))

    if len(result) == 1:
        return result[0]
    else:
        return result


# url/diff/variable_to_differentiate/order/expression
def differentiateExpression(numbers):
    variable_to_differentiate = Symbol(numbers[0])
    order = int(numbers[1])
    expression = "/".join(numbers[2:])
    expression_variables = {ch: Symbol(
        ch) for ch in expression if ch in string.ascii_letters}
    locals().update(expression_variables)
    derivative = diff(expression, variable_to_differentiate, order)
    return str(derivative)


# url/int-indef/variable_to_integrate/expression
def integrateExpressionIndefinite(numbers):
    variable_to_integrate = Symbol(numbers[0])
    expression = "/".join(numbers[1:])
    expression_variables = {ch: Symbol(
        ch) for ch in expression if ch in string.ascii_letters}
    locals().update(expression_variables)
    integral = integrate(expression, variable_to_integrate)
    return str(integral)


# url/int-def/variable_to_integrate/low/high/expression
def integrateExpressionDefinite(numbers):
    variable_to_integrate = Symbol(numbers[0])
    limit_lower = float(numbers[1])
    limit_upper = float(numbers[2])
    expression = "/".join(numbers[3:])
    expression_variables = {ch: Symbol(
        ch) for ch in expression if ch in string.ascii_letters}
    locals().update(expression_variables)
    integral_value = integrate(
        expression, (variable_to_integrate, limit_lower, limit_upper))
    # check type and return - can result in numeric result or equation
    return str(integral_value)


# url/limit/variable_to_limit/limit_value/expression
def getLimit(numbers):
    print(numbers)
    variable_to_limit = Symbol(numbers[0])
    limit_value = numbers[1]

    if '+' in limit_value:
        side = '+'
        limit_value = float(limit_value[:-1])
    elif '-' in limit_value:
        side = '-'
        limit_value = float(limit_value[:-1])
    else:
        side = '+'
        limit_value = float(limit_value)

    expression = "/".join(numbers[2:])
    expression_variables = {ch: Symbol(
        ch) for ch in expression if ch in string.ascii_letters}
    locals().update(expression_variables)
    result = float(limit(expression, variable_to_limit, limit_value, dir=side))
    return result


# url/series/variable_in_series/x0/n/expression
def getSeries(numbers):
    variable_in_series = Symbol(numbers[0])
    x0 = numbers[1]
    n = int(numbers[2])

    if '+' in x0:
        side = '+'
        x0 = float(x0[:-1])
    elif '-' in x0:
        side = '-'
        x0 = float(x0[:-1])
    else:
        side = '+'
        x0 = float(x0)

    expression = "/".join(numbers[3:])
    expression_variables = {ch: Symbol(
        ch) for ch in expression if ch in string.ascii_letters}
    locals().update(expression_variables)
    result = str(series(expression, variable_in_series, x0,
                        n, dir=side))   # take n_terms as input?
    return result


# url/fourier/variable_in_series/n_terms/lower_limit/upper_limit/expression
def getFourierSeries(numbers):
    variable_in_series = Symbol(numbers[0])
    n_terms = int(numbers[1])
    limit_lower = float(numbers[2])
    limit_upper = float(numbers[3])
    expression = "/".join(numbers[4:])
    expression_variables = {ch: Symbol(
        ch) for ch in expression if ch in string.ascii_letters}
    locals().update(expression_variables)
    fourier_value = fourier_series(
        expression, (variable_in_series, limit_lower, limit_upper)).truncate(n_terms)
    return str(fourier_value)
