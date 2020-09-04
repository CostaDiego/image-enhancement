from flask import Flask, request, redirect, abort
from flask import send_file, send_from_directory, safe_join
from flask import render_template, jsonify
import logging
import argparse
import subprocess
import json
import os


_LOG_FILE = 'flaskServer.log'

api = Flask(__name__)

logging.basicConfig(
        filename=_LOG_FILE,
        level=logging.INFO,
        filemode='a',
        format='%(asctime)s %(message)s')

_parser = argparse.ArgumentParser(
    description='Start Flask Server')

_parser.add_argument(
    '-E',
    '--env',
    type=str,
    default='production',
    choices = ['development', 'production', 'testing'],
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


@api.route("/files")
def list_files():
    """Endpoint to list files on the server."""
    files = []
    for filename in os.listdir(api.config['UPLOAD_DIRECTORY']):
        path = os.path.join(api.config['UPLOAD_DIRECTORY'], filename)
        if os.path.isfile(path):
            files.append(filename)
    return jsonify(files)

@api.route("/files/<path:path>", methods=['GET'])
def get_file(path):
    """Download a file."""
    logging.info('Receiving a GET request.')
    logging.info('Requesting file: {}'.format(
        os.path.join(
            api.config['UPLOAD_DIRECTORY'],
            path,
        )
    ))
    return send_from_directory(
                api.config['UPLOAD_DIRECTORY'],
                path,
                as_attachment=True
            )


@api.route("/files/<filename>", methods=['POST'])
def post_file(filename):
    """Upload a file."""
    logging.info('Receiving a POST request.')
    if "/" in filename:
        # Return 400 BAD REQUEST
        logging.warning('Bad Request. No Directories Allowed.')
        abort(400, "No directories allowed")

    with open(os.path.join(api.config['DOWNLOAD_DIRECTORY'], filename), "wb") as fp:
        fp.write(request.data)

    logging.info('File Received: {}'.format(
        os.path.join(
            api.config['DOWNLOAD_DIRECTORY'],
            filename
        )
    ))
    # Return 201 CREATED
    return "", 201


###--------------Future Approach to grant safer way to post images ---------
# @api.route('/upload-image', methods=['GET', 'POST'])
# @api.route('/download-image', methods=['GET', 'POST'])
# def traffic_handler():
#     return request.url
#     return "The request reached the handler method!"
###--------------Future Approach to grant safer way to post images ---------


if __name__ == "__main__": 
    args = _parser.parse_args()

    if args.env.lower() == 'development':
        api.config.from_object("config.DevelopmentConfig")
        logging.info('Loading configuration. ENV: {}'.format(api.config['ENV']))

    if args.env.lower() == 'testing':
        api.config.from_object("config.TestingConfig")
        logging.info('Loading configuration. ENV: {}'.format(api.config['ENV']))

    if args.env.lower() == 'production':
        api.config.from_object("config.ProductionConfig")
        logging.info('Loading configuration. ENV: {}'.format(api.config['ENV']))

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

    