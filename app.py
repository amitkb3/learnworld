from flask import Flask, render_template
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
  lesson_data =  [
    {"id": 1,"lesson_name":"Animals","lesson_image":"lion.jpg","lesson_summary":"Learn about animals"},
    {"id": 2,"lesson_name":"Fruits","lesson_image":"watermelon.jpg","lesson_summary":"Learn about fruits"},   
    {"id": 3,"lesson_name":"Vegetables","lesson_image":"carrot.jpg","lesson_summary":"Learn about vegetables"},
    {"id": 4,"lesson_name":"Birds","lesson_image":"parrot.jpg","lesson_summary":"Learn about birds"},
    {"id": 5,"lesson_name":"Animals 2","lesson_image":"tiger.jpg","lesson_summary":"Learn more about animals"},    
     {"id": 6,"lesson_name":"Fruits 2","lesson_image":"mango.jpg","lesson_summary":"Learn More bout Fruits"},
     {"id": 7,"lesson_name":"Vegetables","lesson_image":"potato.jpg","lesson_summary":"Learn about vegetables"},
    {"id": 8,"lesson_name":"Birds","lesson_image":"eagle.jpg","lesson_summary":"Learn about birds"}
  ]
  return render_template('lessons.html', lesson_data=lesson_data)

# Route handler for card
@app.route('/cards/<int:lesson_id>')
def show_card(lesson_id):

  card_data =  [
    {"id": 1,"card_name":"Lion","card_image":"lion.jpg","english_concept":"lion","hindi_concept":"शेर","lesson_id":1},
    {"id": 2,"card_name":"Zebra","card_image":"zebra.jpg","english_concept":"zebra","hindi_concept":"ज़ेबरा","lesson_id":1},
    {"id": 3,"card_name":"Monkey","card_image":"monkey.jpg","english_concept":"monkey","hindi_concept":"बंदर","lesson_id":1},
    {"id": 4,"card_name":"Cat","card_image":"cat.jpg","english_concept":"cat","hindi_concept":"बिल्ली","lesson_id":1},
    {"id": 5,"card_name":"Donkey","card_image":"donkey.jpg","english_concept":"donkey","hindi_concept":"गधा","lesson_id":1}
  ]

  card_data1 =  [
    {"id": 21,"card_name":"Tiger","card_image":"tiger.jpg","english_concept":"tiger","hindi_concept":"बाघ","lesson_id":5},
    {"id": 22,"card_name":"Horse","card_image":"horse.jpg","english_concept":"horse","hindi_concept":"घोड़ा","lesson_id":5},
    {"id": 23,"card_name":"Dog","card_image":"dog.jpg","english_concept":"dog","hindi_concept":"कुत्ता","lesson_id":5},
    {"id": 24,"card_name":"Elephant","card_image":"elephant.jpg","english_concept":"elephant","hindi_concept":"हाथी","lesson_id":5},
    {"id": 25,"card_name":"Panda","card_image":"panda.jpg","english_concept":"panda","hindi_concept":"पांडा","lesson_id":5}
  ]

  return render_template('cards.html', card_data=card_data)






    

