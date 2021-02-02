import flask
from flask import Flask
from .utils import *


app = Flask(__name__)

function_mapper = {
    "add": addition,
    "sub": subtraction,
    "mul": multiplication,
    "div": division,
    "sin": sine,
    "cos": cosine,
    "tan": tangent,
    "fact": factorialNumber,
    "sort": sortNumbersIncreasing,
    "sort-inc": sortNumbersIncreasing,
    "sort-dec": sortNumbersDecreasing,
    "mat": getMatrices,
    "mat-add": addMatrices,
    "mat-sub": subtractMatrices,
    "diff": differentiateExpression,
    "int-def": integrateExpressionDefinite,
    "int-indef": integrateExpressionIndefinite

}


def getFunctionCall(url):
    function_name = url.split("/")[3]
    function_reference = function_mapper[function_name]
    return function_name, function_reference


@app.route("/", methods=["GET"])
def home(*vargs):
    result = f'''Hello there stranger! It seems you do not know how to use my AaaS. 
    There are currently {COUNTER.value} clients successfully using my AaaS for their apps.
    To learn more about my AaaS, visit https://github.com/aditeyabaral/arithmetic-as-a-service'''
    return result, 200


@app.route("/add/<path:vargs>", methods=["GET"])
@app.route("/sub/<path:vargs>", methods=["GET"])
@app.route("/mul/<path:vargs>", methods=["GET"])
@app.route("/div/<path:vargs>", methods=["GET"])
@app.route("/sin/<path:vargs>", methods=["GET"])
@app.route("/cos/<path:vargs>", methods=["GET"])
@app.route("/tan/<path:vargs>", methods=["GET"])
@app.route("/fact/<path:vargs>", methods=["GET"])
@app.route("/sort/<path:vargs>", methods=["GET"])
@app.route("/sort-inc/<path:vargs>", methods=["GET"])
@app.route("/sort-dec/<path:vargs>", methods=["GET"])
@app.route("/mat/<path:vargs>", methods=["GET"])
@app.route("/mat-add/<path:vargs>", methods=["GET"])
@app.route("/mat-sub/<path:vargs>", methods=["GET"])
@app.route("/diff/<path:vargs>", methods=["GET"])
@app.route("/int-def/<path:vargs>", methods=["GET"])
@app.route("/int-indef/<path:vargs>", methods=["GET"])
def call(vargs):
    function_name, function_reference = getFunctionCall(flask.request.base_url)
    return getFunctionResult(function_reference, vargs)


if __name__ == "__main__":
    app.run()
