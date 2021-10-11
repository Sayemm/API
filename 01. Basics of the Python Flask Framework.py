# Understanding the Basics of the Python Flask Framework and its Workflow

# flask is the package name of flask framework
# Flask is the constructor of the flask application
from flask import Flask, jsonify, request

app = Flask(__name__)


# this application is always listening to '/' 127.0.0.1:5000/
# get the request at / and / tells flask make this function handle the request.
@app.route('/')
def hello_world():
    return 'Hello VAI'


# prepare a response for the request that come to /bye
@app.route('/bye')
def bye():
    c = 522 * 55
    s = str(c)
    return s


@app.route('/add', methods=['POST'])
def add():
    # GET x, y from the data
    dataDict = request.get_json()

    if "y" not in dataDict:
        return "ERROR Y doesn't exist", 305

    x = dataDict["x"]
    y = dataDict["y"]
    z = x + y

    retJSON = {
        "z": z
    }

    return jsonify(retJSON), 200


# prepare a response for the request that come to /json and return JSON
@app.route('/json')
def back():
    number = 2 ** 10
    retJson = {
        'number': number,
        'this is the name of my field': 'abc',
        'string': 'cde',
        'boolean': True,
        'null': None,
        'array': [1, 3, 5, "abcd"],
        'array of objects': [
            {
                'f1': 1
            },
            {
                'f2': "abcd"
            }
        ],
        'nested array': [
            {
                'nested': [
                    {
                        'company': 'nokia',
                        'number': 45454
                    },
                    {
                        'company': 'sony',
                        'number': 1234
                    }
                ]
            }
        ]
    }

    return jsonify(retJson)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)  # We left it empty until we deploy
