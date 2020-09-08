from api.flaskServer import api,_prepareEnv
from os.path import join

api.config.from_object("api.config.ProductionConfig")
_prepareEnv(
            downloadDirectory = join(
                'api',
                api.config['DOWNLOAD_DIRECTORY']
            ),
            uploadDirectory = join(
                'api',
                api.config['UPLOAD_DIRECTORY'])
    )
    
if __name__ == '__main__':
    try:
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