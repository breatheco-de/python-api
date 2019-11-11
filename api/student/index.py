import os
from flask import Flask, request, jsonify, url_for, Blueprint, Response
from flask_swagger import swagger
from flask_cors import CORS


app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=["POST"])
def catch_all(path):
    if request.method=="POST":
        try:
            # student = request.json.get('text')
            request_json = request.json(force=True)
            if request_json == None:
                return jsonify("Student name not provided. Please check your request and try again."),400
            else:
                return jsonify("Success. Received  {}".format(request_json)),200

        except Exception as e:
            return "An exception of type {0} occurred. \nArguments: {1!r}".format(
                type(e).__name__, e.args)
    else:
        return jsonify("You have used an unsupported request type. Please check the type and try again."),404