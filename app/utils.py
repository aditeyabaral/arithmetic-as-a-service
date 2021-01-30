import math
import json
import numpy as np
from multiprocessing import Value

COUNTER = Value("i", 0)


def incrementCounter():
    with COUNTER.get_lock():
        COUNTER.value += 1


def getFunctionResult(function, vargs, **flags):
    incrementCounter()
    numbers = vargs.split("/")
    if not flags:
        result = function(numbers)
    else:
        if function is sortNumbers:
            result = function(numbers, reverse=flags["reverse"])
    result = json.dumps(result)
    return result


def addition(numbers):
    try:
        result = float(numbers[0])
        for num in numbers[1:]:
            result += float(num)
    except:
        return "Bad request", 400
    return result, 200


def subtraction(numbers):
    try:
        result = float(numbers[0])
        for num in numbers[1:]:
            result -= float(num)
    except:
        return "Bad request", 400
    return result, 200


def multiplication(numbers):
    try:
        result = float(numbers[0])
        for num in numbers[1:]:
            result *= float(num)
    except:
        return "Bad request", 400
    return result, 200


def division(numbers):
    try:
        result = float(numbers[0])
        for num in numbers[1:]:
            result /= float(num)
    except:
        return "Bad request", 400
    return result, 200


def sine(numbers):
    try:
        result = list()
        for num in numbers:
            result.append(math.sin(float(num)))
    except:
        return "Bad request", 400

    if len(result) == 1:
        return result[0], 200
    else:
        return result, 200


def cosine(numbers):
    try:
        result = list()
        for num in numbers:
            result.append(math.cos(float(num)))
    except:
        return "Bad request", 400

    if len(result) == 1:
        return result[0], 200
    else:
        return result, 200


def tangent(numbers):
    try:
        result = list()
        for num in numbers:
            result.append(math.tan(float(num)))
    except:
        return "Bad request", 400

    if len(result) == 1:
        return result[0], 200
    else:
        return result, 200


def factorial(numbers):
    try:
        result = list()
        for num in numbers:
            result.append(math.factorial(int(num)))
    except:
        return "Bad request", 400

    if len(result) == 1:
        return result[0], 200
    else:
        return result, 200


def sortNumbers(numbers, reverse=False):
    numbers = list(map(float, numbers))
    result = list(map(str, sorted(numbers, reverse=reverse)))
    return result, 200


'''def getMatrix(numbers):
    numbers = list(map(float, numbers))
    ndims = int(numbers[0])
    dims = [int(numbers[i]) for i in range(1, 1+ndims)]
    matrix = np.reshape(numbers[ndims+1:], dims)
    return matrix.tolist()'''


def getMatrices(numbers):  # url/nmatrices/ndims/dim1/.../dimn/num1...
    numbers = list(map(float, numbers))
    nmatrices = int(numbers[0])
    ndims = int(numbers[1])
    dims = [int(numbers[i]) for i in range(2, 2+ndims)]
    matrix_values = np.split(np.asarray(numbers[2+ndims:]), nmatrices)
    matrices = [np.reshape(m, dims).tolist() for m in matrix_values]
    return matrices


def addMatrices(numbers):
    matrices = getMatrices(numbers)
    result = np.add(*matrices).tolist()
    return result

def subtractMatrices(numbers):
    matrices = getMatrices(numbers)
    result = np.subtract(*matrices).tolist()
    return result
