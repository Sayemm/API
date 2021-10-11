# Understanding and Implementing a Simple REST API

from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


def checkPostedData(postedData, functionName):
    if functionName == "add" or functionName == "subtract" or functionName == "multiply":
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200

    elif functionName == "division":
        if "x" not in postedData or "y" not in postedData:
            return 301
        elif postedData["y"] == 0:
            return 302
        else:
            return 200


class Add(Resource):
    def post(self):
        # get the data
        postedData = request.get_json()

        # Verify Validity
        status_code = checkPostedData(postedData, "add")
        if status_code != 200:
            retJson = {
                "Message": "An Error Happened",
                "Status Code": status_code
            }
            return jsonify(retJson)

        # If here then status code == 200
        x = postedData["x"]
        y = postedData["y"]

        x = int(x)
        y = int(y)

        retJson = {
            "Message": x + y,
            "Status Code": 200
        }
        return jsonify(retJson)


class Subtract(Resource):
    def post(self):
        # get the data
        postedData = request.get_json()

        # Verify Validity
        status_code = checkPostedData(postedData, "subtract")
        if status_code != 200:
            retJson = {
                "Message": "An Error Happened",
                "Status Code": status_code
            }
            return jsonify(retJson)

        # If here then status code == 200
        x = postedData["x"]
        y = postedData["y"]

        x = int(x)
        y = int(y)

        retJson = {
            "Message": x - y,
            "Status Code": 200
        }
        return jsonify(retJson)


class Multiply(Resource):
    def post(self):
        # get the data
        postedData = request.get_json()

        # Verify Validity
        status_code = checkPostedData(postedData, "multiply")

        if status_code != 200:
            retJson = {
                "Message": "An Error Happened",
                "Status Code": status_code
            }
            return jsonify(retJson)

        # If here then status code == 200
        x = postedData["x"]
        y = postedData["y"]

        x = int(x)
        y = int(y)

        retJson = {
            "Message": x * y,
            "Status Code": 200
        }
        return jsonify(retJson)


class Divide(Resource):
    def post(self):
        # get the data
        postedData = request.get_json()

        # Verify Validity
        status_code = checkPostedData(postedData, "division")

        if status_code != 200:
            retJson = {
                "Message": "An Error Happened",
                "Status Code": status_code
            }
            return jsonify(retJson)

        # If here then status code == 200
        x = postedData["x"]
        y = postedData["y"]

        x = int(x)
        y = int(y)

        retJson = {
            "Message": (x * 1.0) / y,
            "Status Code": 200
        }
        return jsonify(retJson)


api.add_resource(Add, "/add")
api.add_resource(Subtract, "/sub")
api.add_resource(Multiply, "/mul")
api.add_resource(Divide, "/div")


@app.route('/')
def hello():
    return "OKAY"


if __name__ == "__main__":
    app.run()
