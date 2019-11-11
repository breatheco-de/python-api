import os
from flask import Flask, request, jsonify, url_for, Blueprint, Response
from flask_swagger import swagger
from flask_cors import CORS

app = Flask(__name__)
student_endpoint = "https://api.breatheco.de/api/student/"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=["POST"])
def catch_all(path):
    if request.method=="POST":
        try:
            request_form = request.form['text']
            if request_form == None:
                return jsonify("Command not provided. Please check your request and try again."),400
            parsed_request = request_form.split(' ')
            if parsed_request[0].lower()=="student":
                # <email>?access_token=<token>
                return jsonify("Success. Received  {}".format(parsed_request[1])),200
            else:
                return jsonify("Invalid Request. Try the syntax '/4geeks student <email>'")

        except Exception as e:
            return "An exception of type {0} occurred. \nArguments: {1!r}".format(
                type(e).__name__, e.args)
    else:
        return jsonify("You have used an unsupported request type. Please check the type and try again."),404