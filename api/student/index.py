import os
from flask import Flask, request, jsonify, url_for, Blueprint, Response
# from flask_dotenv import DotEnv
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
# from api.user.model import db,User


app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=["GET"])
def catch_all(path):
    if request.method=="GET":
        try:
            student = request.args.get('text')
            if student == None:
                return Response("Student name not provided. Please check your request and try again."),400
            return Response("Success. Student:  {}".format(student)),200

        except Exception as e:
            return "An exception of type {0} occurred. \nArguments: {1!r}".format(
                type(e).__name__, e.args)
    else:
        return Response("You have used an unsupported request type. Please check the type and try again."),404