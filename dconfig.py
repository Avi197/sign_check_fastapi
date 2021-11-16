import os


class Config(object):
    pass


class ProductionConfig(Config):
    DEBUG = False
    LOG_DIR = os.getenv('LOG_DIR')  # để devops tự config
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEVICE = os.getenv('DEVICE')
    VND_ID_INTERNAL_DOMAIN = os.getenv('VND_ID_DOMAIN')  # 'https://vndid-int-api.vndirect.com.vn/'

    SERVER_NAME = os.getenv('SERVER_NAME')
    PORT_NUMBER = os.getenv('PORT_NUMBER')
    DATA_DIR = os.getenv('DATA_DIR')
    YOLO_DIR = os.getenv('YOLO_DIR')
    FLASK_APP = os.getenv('FLASK_APP')
    NUM_TORCH_THREADS = os.getenv('NUM_TORCH_THREADS')


class DevelopmentConfig(Config):
    DEBUG = True
    LOG_DIR = 'log'
    SECRET_KEY = 'dev'

    VND_ID_INTERNAL_DOMAIN = 'https://accounts-uat.vndirect.com.vn/'
    if os.getenv('SERVER_NAME'):
        SERVER_NAME = os.getenv('SERVER_NAME')
    else:
        SERVER_NAME = "0.0.0.0"
    if os.getenv('PORT_NUMBER'):
        PORT_NUMBER = os.getenv('PORT_NUMBER')
    else:
        PORT_NUMBER = 5000

    if os.getenv('DATA_DIR'):
        DATA_DIR = os.getenv('DATA_DIR')
    else:
        DATA_DIR = '/home/phamson/gitlab/signature_checking/data'
    if os.getenv('YOLO_DIR'):
        YOLO_DIR = os.getenv('YOLO_DIR')
    else:
        YOLO_DIR = '/home/phamson/gitlab/signature_checking/datayolov5'
    NUM_TORCH_THREADS = os.getenv('NUM_TORCH_THREADS')
    if os.getenv('DEVICE') and (os.getenv('DEVICE') == 'cuda' or os.getenv('DEVICE') == 'cpu'):
        DEVICE = os.getenv('DEVICE')
    else:
        DEVICE = 'cpu'
    FLASK_APP = 'ocr_api'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}

VERSION = "1.0.1"

config_object = config[os.getenv('FLASK_ENV') or 'development']
