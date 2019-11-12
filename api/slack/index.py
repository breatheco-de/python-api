import os,re,json,requests,urllib.parse,sys
from flask import Flask, request, jsonify, url_for, Blueprint, Response
from flask_swagger import swagger
from flask_cors import CORS

app = Flask(__name__)
api = "https://api.breatheco.de/api/"

client_id = os.environ.get('BREATHECODE_CLIENT_ID')
client_secret = os.environ.get('BREATHECODE_CLIENT_SECRET')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=["POST"])
def catch_all(path):
    if request.method=="POST":
        try:
            # Request comes as formdata
            request_form = request.form['text']
            if request_form == None:
                return jsonify("Command not provided. Please check your request and try again."),400
            parsed_request = request_form.split(' ')
            if parsed_request[0].lower()=="student": #check if command was "student"
                email = parsed_request[1] # this is the email address
                regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
                if re.search(regex,email):
                    # student_endpoint/<email>?access_token=<token>
                    token=get_token()
                    if token:
                        endpoint = api+"student/"+urllib.parse.quote_plus(email)+"?access_token="+token
                        api_response = requests.get(endpoint).json()
                        data = api_response["data"]
                        json_to_send = {
                            "full_name": data["first_name"]+" "+data["last_name"],
                            "cohorts": data["cohorts"],
                            "github_username": data["github"],
                            "status": data["status"],
                            "financial_status": data["financial_status"],
                            "phone": data["phone"],
                            "student_external_profile": data["internal_profile_url"]
                        }
                        return jsonify(json_to_send),200
                    else:
                        return jsonify("msg","Invalid Token"),401
                    
                else:
                    return jsonify("Email address did not have valid format."),510

                
                return jsonify("Success. Received  {}".format()),200
            else:
                return jsonify("Invalid Request. Try the syntax '/4geeks student <email>'")

        except Exception as e:
            exc_type, exc_obj, tb = sys.exc_info()
            f = tb.tb_frame
            lineno = tb.tb_lineno
            filename = f.f_code.co_filename
            return "An exception of type {0} occurred. \nArguments: {1!r} \nFile: {2}\nLine: {3}".format(
                type(e).__name__, e.args,filename,lineno)
    else:
        return jsonify("You have used an unsupported request type. Please check the type and try again."),404

def get_token():
    token_endpoint = api+"token"
    data = {
        "grant_type":"client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }
    try:
        token_response = requests.post(token_endpoint, json = data)
        if token_response.status_code==200:
            resp_dict = json.loads(token_response.text)
            return resp_dict['access_token']
        else:
            return token_response
    except Exception as e:
            exc_type, exc_obj, tb = sys.exc_info()
            f = tb.tb_frame
            lineno = tb.tb_lineno
            filename = f.f_code.co_filename
            return "An exception of type {0} occurred. \nArguments: {1!r} \nFile: {2}\nLine: {3}".format(
                type(e).__name__, e.args,filename,lineno)