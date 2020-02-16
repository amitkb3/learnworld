import os

class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
  # Database URI
  SQLALCHEMY_DATABASE_URI = 'postgres+pyscopg2://postgres:postgres@localhost:5432/learnworld'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  
