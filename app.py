from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from flask_sqlalchemy import SQLAlchemy


from config import Config
from forms import *

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from models import Lesson, Card

@app.route('/healthy')
def healthy():
  return 'Healthy'

@app.route('/')
@app.route('/index')
def lessons():
  lesson_data =  [
    {"id": 1,"lesson_name":"Animals","lesson_image":"lion.jpg","lesson_summary":"Learn about animals"},
    {"id": 2,"lesson_name":"Fruits","lesson_image":"watermelon.jpg","lesson_summary":"Learn about fruits"},   
    {"id": 3,"lesson_name":"Vegetables","lesson_image":"carrot.jpg","lesson_summary":"Learn about vegetables"},
    {"id": 4,"lesson_name":"Birds","lesson_image":"parrot.jpg","lesson_summary":"Learn about birds"},
    {"id": 5,"lesson_name":"Animals 2","lesson_image":"tiger.jpg","lesson_summary":"Learn more about animals"},    
     {"id": 6,"lesson_name":"Fruits 2","lesson_image":"mango.jpg","lesson_summary":"Learn more bout Fruits"},
     {"id": 7,"lesson_name":"Vegetables 2","lesson_image":"potato.jpg","lesson_summary":"Learn more about vegetables"},
    {"id": 8,"lesson_name":"Birds 2","lesson_image":"eagle.jpg","lesson_summary":"Learn about birds"}
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

# Create Lesson
# -------------------

# Get the Create Lesson Form
@app.route('/lessons/create', methods=['GET'])
def create_lesson_form():
  form = LessonForm()
  return render_template('forms/new_lesson.html', form=form)

# Post handler for Leasson Creation
@app.route('/lessons/create', methods=['POST'])
def create_lesson_submission():
  try:
    form = LessonForm()
    lesson_name = form.lesson_name.data
    lesson_image = form.lesson_image.data
    lesson_summary = form.lesson_summary.data

    lesson = Lesson(lesson_name=lesson_name,
    lesson_image=lesson_image,
    lesson_summary=lesson_summary
    )

    db.session.add(lesson)
    db.session.commit()
    # on successful db insert, flash success
    flash('Lesson ' + request.form['lesson_name'] + ' was successfully added.')
  except:
    db.session.rollback()
    flash('An error occured. Lesson ' + request.form['lesson_name'] + ' could not be added.')
  finally:
    db.session.close()
  return redirect(url_for('lessons'))

# Create Card
# -------------------

# Get the Create Card Form
@app.route('/cards/create', methods=['GET'])
def create_card_form():
  form = CardForm()
  return render_template('forms/new_card.html', form=form)



    

