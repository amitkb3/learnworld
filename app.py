from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from models import Lesson, Card

@app.route('/healthy')
def healthy():
  return 'Healthy'

@app.route('/')
def lessons():
  lesson_data = data = [
    {"id": 1,"lesson_name":"Animals","lesson_image":"lion.jpg","lesson_summary":"Learn about animals"},
    ,
    {"id": 2,"lesson_name":"Fruits","lesson_image":"watermelon.jpg","lesson_summary":"Learn about fruits"},   
    {"id": 3,"lesson_name":"Vegetables","lesson_image":"carrot.jpg","lesson_summary":"Learn about vegetables"},
    {"id": 4,"lesson_name":"Birds","lesson_image":"parrot.jpg","lesson_summary":"Learn about birds"}
    {"id": 5,"lesson_name":"Animals 2","lesson_image":"tiger.jpg","lesson_summary":"Learn more about animals"}    
     {"id": 6,"lesson_name":"Fruits 2","lesson_image":"mango.jpg","lesson_summary":"Learn More bout Fruits"},
     {"id": 7,"lesson_name":"Vegetables","lesson_image":"potato.jpg","lesson_summary":"Learn about vegetables"},
    {"id": 8,"lesson_name":"Birds","lesson_image":"eagle.jpg","lesson_summary":"Learn about birds"}
  ]
  return render_template('lessons.html', data=lesson_data)

