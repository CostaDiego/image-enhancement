from flask import Flask
from flask import request
import requests
import subprocess
import json
import time


PORT = 8123
HOST = 'localhost'

app = Flask(__name__)


@app.route("/", methods=['POST'])
def index():
    return "Relow"

def notify(message):
    payload = {'text' : message}
    r = requests.post(payload_url, data=json.dumps(payload))

def execute_script(script):
    cmd = ["powershell","-ExecutionPolicy", "Bypass", "C:\\deploy\\{0}.ps1".format(script)]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    out,err = p.communicate()
    if(err):
        raise Exception('Error: ' + str(err))
    return out

if __name__ == "__main__":
    app.run(port = PORT, host = HOST, debug=True, threaded=True)