from flask import Flask, request, abort, jsonify
from flask import send_file, send_from_directory, safe_join
import logging
import argparse
import subprocess
import json
import time
import os

api = Flask(__name__)
# api.config.from_object("config.DevelopmentConfig")

parser = argparse.ArgumentParser(
    description='Start Flask Server')

parser.add_argument(
    '-E',
    '--env',
    type=str,
    default='production',
    choices = ['development', 'production'],
    help='The local where the image will be saved.')

def _prepareEnv(downloadDirectory = None, uploadDirectory = None):
    logging.info('Performing Environment Check')
    response = {'DOWNLOAD': None, 'UPLOAD': None}

    if downloadDirectory and not os.path.exists(downloadDirectory):
        os.makedirs(downloadDirectory)
        response['DOWNLOAD'] = downloadDirectory
        logging.info('Create Directory: {}'.format(response['DOWNLOAD']))

    if uploadDirectory and not os.path.exists(uploadDirectory):
        os.makedirs(uploadDirectory)
        response['UPLOAD'] = uploadDirectory
        logging.info('Create Directory: {}'.format(response['UPLOAD']))

    return (True if response['DOWNLOAD'] else False,
            True if response['UPLOAD'] else False)

@api.route("/", methods=['GET'])
def hello():
    response = "Hello, If you are seeing this, means the server is online!\n"
    return response

if __name__ == "__main__":
    logging.basicConfig(
        filename='flaskServer.log',
        level=logging.INFO,
        format='%(asctime)s %(message)s')

    args = parser.parse_args()

    if args.env.lower() == 'development':
        api.config.from_object("config.DevelopmentConfig")
        # logging.info('Loading configuration. ENV: {}'.format(api.config['ENV']))

    if args.env.lower() == 'testing':
        api.config.from_object("config.TestingConfig")
        # logging.info('Loading configuration. ENV: {}'.format(api.config['ENV']))

    if args.env.lower() == 'production':
        api.config.from_object("config.ProductionConfig")
        # logging.info('Loading configuration. ENV: {}'.format(api.config['ENV']))

    try:
        _prepareEnv(
            downloadDirectory = api.config['DOWNLOAD_DIRECTORY'],
            uploadDirectory = api.config['UPLOAD_DIRECTORY'])

        logging.info('Starting Service on Port {}'.format(api.config['PORT']))

        api.run(
        port=api.config['PORT'],
        host= api.config['HOST'],
        threaded=api.config['THREADED'])

    except KeyboardInterrupt:
        logging.warning('Stoping Service...')
    
    except Exception as err:
        logging.warning('An Error Occured...')
        logging.error('The Following Error Occured: {}'.format(err))

    finally:
        logging.info('Server Down.')

    