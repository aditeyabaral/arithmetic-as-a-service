from .utils import *
from flask import Flask


app = Flask(__name__)


@app.route("/", methods=["GET"])
def home(*vargs):
    s = f'''Hello there stranger! It seems you do not know how to use my AaaS. 
    There are currently {COUNTER.value} clients successfully using my AaaS for their apps.
    To learn more about my AaaS, visit https://github.com/aditeyabaral/arithmetic-as-a-service'''
    return s, 200


@app.route("/add/<path:vargs>", methods=["GET"])
def add(vargs):
    return getFunctionResult(addition, vargs)


@app.route("/sub/<path:vargs>", methods=["GET"])
def sub(vargs):
    return getFunctionResult(subtraction, vargs)


@app.route("/mul/<path:vargs>", methods=["GET"])
def mul(vargs):
    return getFunctionResult(multiplication, vargs)


@app.route("/div/<path:vargs>", methods=["GET"])
def div(vargs):
    return getFunctionResult(division, vargs)


@app.route("/sin/<path:vargs>", methods=["GET"])
def sin(vargs):
    return getFunctionResult(sine, vargs)


@app.route("/cos/<path:vargs>", methods=["GET"])
def cos(vargs):
    return getFunctionResult(cosine, vargs)


@app.route("/tan/<path:vargs>", methods=["GET"])
def tan(vargs):
    return getFunctionResult(tangent, vargs)


@app.route("/fact/<path:vargs>", methods=["GET"])
def fact(vargs):
    return getFunctionResult(factorial, vargs)


@app.route("/sort/<path:vargs>", methods=["GET"])
def sortOrder(vargs):
    return getFunctionResult(sortNumbers, vargs)


@app.route("/sort/increasing/<path:vargs>", methods=["GET"])
def sortIncreasingOrder(vargs):
    return getFunctionResult(sortNumbers, vargs)


@app.route("/sort/decreasing/<path:vargs>", methods=["GET"])
def sortDecreasingOrder(vargs):
    return getFunctionResult(sortNumbers, vargs, reverse=True)


@app.route("/matrix/<path:vargs>", methods=["GET"])
def createMatrix(vargs):
    return getFunctionResult(getMatrices, vargs)


@app.route("/add-matrix/<path:vargs>", methods=["GET"])
def additionMatrix(vargs):
    return getFunctionResult(addMatrices, vargs)


@app.route("/sub-matrix/<path:vargs>", methods=["GET"])
def subtractionMatrix(vargs):
    return getFunctionResult(subtractMatrices, vargs)


if __name__ == "__main__":
    app.run()
