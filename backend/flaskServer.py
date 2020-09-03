from flask import Flask, jsonify
from flask import request, send_file, send_from_directory, safe_join, abort
import subprocess
import json
import time
import os

# PORT = 8123
# HOST = 'localhost'

api = Flask(__name__)
api.config.from_object("config.DevelopmentConfig")

def _prepareEnv():
    pass

@api.route("/", methods=['GET'])
def index():
    return api.config['SECRET_KEY']

if __name__ == "__main__":
    # api.run(port = PORT, host = HOST, debug=True, threaded=True)
    api.run(port=api.config['PORT'], host= api.config['HOST'])