from flask import Flask
from flask import request
from flask import Response
import json
import lambda_function

# arn:aws:lambda:eu-west-1:095485643790:function:RNV

app = Flask(__name__)

long_output = True


@app.route('/status', methods=['GET', 'POST'])
def status():
    return 'OK'


@app.route("/", methods=['GET'])
def get_resp():
    return 'OK'


@app.route("/", methods=['POST'])
def inital():
    incoming_data = request.data.decode('utf-8')
    incoming_data = json.loads(incoming_data)
    respond_json = lambda_function.lambda_handler(incoming_data)
    respond_json = json.dumps(respond_json, ensure_ascii=False)
    resp = Response(respond_json)
    return resp


if __name__ == "__main__":
    app.run(debug=True)