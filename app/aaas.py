import .utils
from flask import Flask
from multiprocessing import Value

COUNTER = Value("i", 0)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home(*vargs):
    s = f'''Hello there stranger! It seems you do not know how to use my AaaS. 
    There are currently {COUNTER.value} clients successfully using my AaaS for their apps.
    To learn more about my AaaS, visit https://github.com/aditeyabaral/arithmetic-as-a-service'''
    return s, 200


@app.route("/add/<path:vargs>", methods=["GET"])
def add(vargs):
    with COUNTER.get_lock():
        COUNTER.value += 1
    numbers = vargs.split("/")
    result = utils.addition(numbers)
    return result


@app.route("/sub/<path:vargs>", methods=["GET"])
def sub(vargs):
    with COUNTER.get_lock():
        COUNTER.value += 1
    numbers = vargs.split("/")
    result = utils.subtraction(numbers)
    return result


@app.route("/mul/<path:vargs>", methods=["GET"])
def mul(vargs):
    with COUNTER.get_lock():
        COUNTER.value += 1
    numbers = vargs.split("/")
    result = utils.multiplication(numbers)
    return result


@app.route("/div/<path:vargs>", methods=["GET"])
def div(vargs):
    with COUNTER.get_lock():
        COUNTER.value += 1
    numbers = vargs.split("/")
    result = utils.division(numbers)
    return result


@app.route("/sin/<path:vargs>", methods=["GET"])
def sin(vargs):
    with COUNTER.get_lock():
        COUNTER.value += 1
    numbers = vargs.split("/")
    result = utils.sine(numbers)
    return result


@app.route("/cos/<path:vargs>", methods=["GET"])
def cos(vargs):
    with COUNTER.get_lock():
        COUNTER.value += 1
    numbers = vargs.split("/")
    result = utils.cosine(numbers)
    return result


@app.route("/tan/<path:vargs>", methods=["GET"])
def tan(vargs):
    with COUNTER.get_lock():
        COUNTER.value += 1
    numbers = vargs.split("/")
    result = utils.tangent(numbers)
    return result


@app.route("/fact/<path:vargs>", methods=["GET"])
def fact(vargs):
    with COUNTER.get_lock():
        COUNTER.value += 1
    numbers = vargs.split("/")
    result = utils.factorial(numbers)
    return result


if __name__ == "__main__":
    app.run()
