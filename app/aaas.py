import flask
from datetime import datetime
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_table import Table, Col
from .utils import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://iwcgggkkrqwldt:9d6eb721bc8243d3a74ef878469ac2cc9e5701306c23e69f6018c5d6a77f9e3f@ec2-3-222-11-129.compute-1.amazonaws.com:5432/d4g3sagup0iaa6"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

function_mapper = {
    "add": addition,
    "sub": subtraction,
    "mul": multiplication,
    "div": division,
    "sin": sine,
    "cos": cosine,
    "tan": tangent,
    "fact": factorialNumber,
    "exp": exponent,
    "log": logarithm,
    "ln": natural_log,
    "sort": sortNumbersIncreasing,
    "sort-inc": sortNumbersIncreasing,
    "sort-dec": sortNumbersDecreasing,
    "mat": getMatrices,
    "mat-add": addMatrices,
    "mat-sub": subtractMatrices,
    "diff": differentiateExpression,
    "int-def": integrateExpressionDefinite,
    "int-indef": integrateExpressionIndefinite,
    "limit": getLimit,
    "series": getSeries,
    "fourier": getFourierSeries
}

db = SQLAlchemy(app)


class Record(db.Model):
    __tablename__ = "logging"
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.DateTime, nullable=False)
    ip = db.Column(db.String(20), nullable=False)
    # name = db.Column(db.String(100), nullable=False)  # get language, version as well?
    browser = db.Column(db.String(100), nullable=False)
    platform = db.Column(db.String(30), nullable=False)
    site = db.Column(db.String(15), nullable=False)

    def __init__(self, site_name):
        self.site = site_name
        self.time = datetime.utcnow()
        self.ip = request.headers.getlist("X-Forwarded-For")[0]
        self.platform = request.user_agent.platform
        self.browser = request.user_agent.browser


class loggingInfoTable(Table):
    __id = Col("__id", show=False)
    time = Col("time")
    ip = Col("ip")
    browser = Col("browser")
    platform = Col("platform")
    site = Col("site")


def getFunctionCall(url):
    function_name = url.split("/")[3]
    function_reference = function_mapper[function_name]
    return function_name, function_reference


def incrementCounter(function_name):
    with COUNTER.get_lock():
        COUNTER.value += 1
    data = Record(function_name)
    db.session.add(data)
    db.session.commit()


def getCounter():
    result = db.session.query(Record).count()
    return result


@app.route("/", methods=["GET"])
def home(*vargs):
    incrementCounter("home")
    total_accesses = getCounter()
    print(total_accesses)
    result = f'''Hello stranger!<br/>
    It seems you do not know how to use my AaaS.<br/>
    My AaaS has been used by over {total_accesses} clients for their daily needs.
    In fact, there are currently {COUNTER.value} active clients successfully using my AaaS for their applications!<br/>
    What are you waiting for? Join all these developers and start useing my AaaS today!<br/>
    To learn more about my AaaS, visit https://github.com/aditeyabaral/arithmetic-as-a-service'''
    return result, 200


@app.route("/logging", methods=["GET"])
def getLogging(*vargs):
    result = db.session.query(Record).all()
    table = loggingInfoTable(result)
    table.border = True
    return render_template("table.html", table=table), 200


@app.route("/add/<path:vargs>", methods=["GET"])
@app.route("/sub/<path:vargs>", methods=["GET"])
@app.route("/mul/<path:vargs>", methods=["GET"])
@app.route("/div/<path:vargs>", methods=["GET"])
@app.route("/sin/<path:vargs>", methods=["GET"])
@app.route("/cos/<path:vargs>", methods=["GET"])
@app.route("/tan/<path:vargs>", methods=["GET"])
@app.route("/fact/<path:vargs>", methods=["GET"])
@app.route("/exp/<path:vargs>", methods=["GET"])
@app.route("/log/<path:vargs>", methods=["GET"])
@app.route("/ln/<path:vargs>", methods=["GET"])
@app.route("/sort/<path:vargs>", methods=["GET"])
@app.route("/sort-inc/<path:vargs>", methods=["GET"])
@app.route("/sort-dec/<path:vargs>", methods=["GET"])
@app.route("/mat/<path:vargs>", methods=["GET"])
@app.route("/mat-add/<path:vargs>", methods=["GET"])
@app.route("/mat-sub/<path:vargs>", methods=["GET"])
@app.route("/diff/<path:vargs>", methods=["GET"])
@app.route("/int-def/<path:vargs>", methods=["GET"])
@app.route("/int-indef/<path:vargs>", methods=["GET"])
@app.route("/limit/<path:vargs>", methods=["GET"])
@app.route("/series/<path:vargs>", methods=["GET"])
@app.route("/fourier/<path:vargs>", methods=["GET"])
def call(vargs):
    function_name, function_reference = getFunctionCall(flask.request.base_url)
    incrementCounter(function_name)
    return getFunctionResult(function_reference, vargs)


if __name__ == "__main__":
    app.run()
