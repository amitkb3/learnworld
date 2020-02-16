from flask import Flask
from flask_sqlalchemy import SQLALchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

@app.route('/healthy')
def healthy():
  return 'Healthy'