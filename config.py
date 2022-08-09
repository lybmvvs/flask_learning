import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'will-learn-flask-and-db-sometime'