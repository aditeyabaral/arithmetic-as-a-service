import math
from flask import Flask
from multiprocessing import Value

COUNTER = Value("i", 0)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home(*vargs):
    s = f'''Hello there stranger! It seems you do not know how to use my AaaS. There are currenly {COUNTER.value} clients successfully using my AaaS for their apps.
    To learn more about my AaaS, visit https://github.com/aditeyabaral/arithmetic-as-a-service'''
    return s


@app.route("/add/<path:vargs>", methods=["GET"])
def add(vargs):
    with COUNTER.get_lock():
        COUNTER.value += 1
    try:
        numbers = list(map(float, vargs.split("/")))
        result = numbers[0]
        for num in numbers[1:]:
            result += num
    except:
        return "Bad request", 400
    return str(result), 200


@app.route("/sub/<path:vargs>", methods=["GET"])
def sub(vargs):
    with COUNTER.get_lock():
        COUNTER.value += 1
    try:
        numbers = list(map(float, vargs.split("/")))
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
    except:
        return "Bad request", 400
    return str(result), 200


@app.route("/mul/<path:vargs>", methods=["GET"])
def mul(vargs):
    with COUNTER.get_lock():
        COUNTER.value += 1
    try:
        numbers = list(map(float, vargs.split("/")))
        result = numbers[0]
        for num in numbers[1:]:
            result *= num
    except:
        return "Bad request", 400
    return str(result), 200


@app.route("/div/<path:vargs>", methods=["GET"])
def div(vargs):
    with COUNTER.get_lock():
        COUNTER.value += 1
    try:
        numbers = list(map(float, vargs.split("/")))
        result = numbers[0]
        for num in numbers[1:]:
            result /= num
    except:
        return "Bad request", 400
    return str(result), 200


@app.route("/sin/<path:vargs>", methods=["GET"])
def sin(vargs):
    with COUNTER.get_lock():
        COUNTER.value += 1
    try:
        numbers = list(map(float, vargs.split("/")))
        result = list()
        for num in numbers:
            result.append(str(math.sin(num)))
    except:
        return "Bad request", 400
    return f"[{', '.join(result)}]", 200


if __name__ == "__main__":
    app.run()
