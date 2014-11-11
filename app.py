# We need to import the jsonify object, it will let us
# output json, and it will take care of the right string
# data conversion, the headers for the response, etc
from flask import Flask, jsonify

# Initialize the Flask application
app = Flask(__name__)


# This route will return a list in JSON format
@app.route('/')
def index():
    # This is a dummy list, 2 nested arrays containing some
    # params and values
    data = {"result": "This is a test reponse from OCR backend"}
    # jsonify will do for us all the work, returning the
    # previous data structure in JSON
    return jsonify(results=data)

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("3000")
    )
