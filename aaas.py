from flask import Flask, request

app = Flask(__name__)


@app.route("/add/<path:vargs>", methods=["GET"])
def add(vargs):
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
    try:
        numbers = list(map(float, vargs.split("/")))
        result = numbers[0]
        for num in numbers[1:]:
            result /= num
    except:
        return "Bad request", 400
    return str(result), 200


if __name__ == "__main__":
    app.run()
