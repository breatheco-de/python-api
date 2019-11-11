from flask import Flask,Response
app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
	return Response("You have reached an unsupported route. Please check the route and try again."),404
