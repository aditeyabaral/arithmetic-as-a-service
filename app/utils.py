import math
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
    return result


def addition(numbers):
    try:
        result = float(numbers[0])
        for num in numbers[1:]:
            result += float(num)
    except:
        return "Bad request", 400
    return str(result), 200


def subtraction(numbers):
    try:
        result = float(numbers[0])
        for num in numbers[1:]:
            result -= float(num)
    except:
        return "Bad request", 400
    return str(result), 200


def multiplication(numbers):
    try:
        result = float(numbers[0])
        for num in numbers[1:]:
            result *= float(num)
    except:
        return "Bad request", 400
    return str(result), 200


def division(numbers):
    try:
        result = float(numbers[0])
        for num in numbers[1:]:
            result /= float(num)
    except:
        return "Bad request", 400
    return str(result), 200


def sine(numbers):
    try:
        result = list()
        for num in numbers:
            result.append(str(math.sin(float(num))))
    except:
        return "Bad request", 400

    if len(result) == 1:
        return result[0], 200
    else:
        return f"[{', '.join(result)}]", 200


def cosine(numbers):
    try:
        result = list()
        for num in numbers:
            result.append(str(math.cos(float(num))))
    except:
        return "Bad request", 400

    if len(result) == 1:
        return result[0], 200
    else:
        return f"[{', '.join(result)}]", 200


def tangent(numbers):
    try:
        result = list()
        for num in numbers:
            result.append(str(math.tan(float(num))))
    except:
        return "Bad request", 400

    if len(result) == 1:
        return result[0], 200
    else:
        return f"[{', '.join(result)}]", 200


def factorial(numbers):
    try:
        result = list()
        for num in numbers:
            result.append(str(math.factorial(int(num))))
    except:
        return "Bad request", 400

    if len(result) == 1:
        return result[0], 200
    else:
        return f"[{', '.join(result)}]", 200


def sortNumbers(numbers, reverse=False):
    numbers = list(map(float, numbers))
    result = list(map(str, sorted(numbers, reverse=reverse)))
    return f"[{', '.join(result)}]", 200
