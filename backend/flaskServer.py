from flask import Flask, jsonify
from flask import request, send_file, send_from_directory, safe_join, abort
import subprocess
import json
import time


PORT = 8123
HOST = '0.0.0.0'

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return jsonify({"message":"Hello Json!"})

if __name__ == "__main__":
    app.run(port = PORT, host = HOST, debug=True, threaded=True)