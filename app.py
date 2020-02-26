from flask import Flask, render_template, request, redirect, url_for, jsonify, flash, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.exceptions import HTTPException
from config import Config
from forms import *

app = Flask(__name__)
app.config.from_object(Config)
CORS(app, resources={r"/*": {"origins": "*"}})
db = SQLAlchemy(app)

from models import Lesson, Card

# CORS Headers
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization,true')
  response.headers.add('Access-Control-Allow-Methods','GET,PUT,POST,DELETE,OPTIONS')
  return response

@app.route('/healthy')
def healthy():
  """
  Route to check health of app
  :returns a text message 'healthy'
  """
  return 'Healthy'

@app.route('/')
@app.route('/index')
def lessons():
  """
  Creates a list of all lessons
  :returns a list of lesson
  """
  try:
    lesson_data = db.session.query(Lesson).all()
    return render_template('lessons.html', lesson_data=lesson_data)
  except:
    abort(422)
  # lesson_data =  [
  #   {"id": 1,"lesson_name":"Animals","lesson_image":"lion.jpg","lesson_summary":"Learn about animals"},
  #   {"id": 2,"lesson_name":"Fruits","lesson_image":"watermelon.jpg","lesson_summary":"Learn about fruits"},   
  #   {"id": 3,"lesson_name":"Vegetables","lesson_image":"carrot.jpg","lesson_summary":"Learn about vegetables"},
  #   {"id": 4,"lesson_name":"Birds","lesson_image":"parrot.jpg","lesson_summary":"Learn about birds"},
  #   {"id": 5,"lesson_name":"Animals 2","lesson_image":"tiger.jpg","lesson_summary":"Learn more about animals"},    
  #    {"id": 6,"lesson_name":"Fruits 2","lesson_image":"mango.jpg","lesson_summary":"Learn more bout Fruits"},
  #    {"id": 7,"lesson_name":"Vegetables 2","lesson_image":"potato.jpg","lesson_summary":"Learn more about vegetables"},
  #   {"id": 8,"lesson_name":"Birds 2","lesson_image":"eagle.jpg","lesson_summary":"Learn about birds"}
  # ]
  

#Route Handler for Admin Page
@app.route('/admin')
def admin():
  """
  Renders admin page where user can login
  and perform Create, Edit and Delete operations
  on Lessons and Cards
  :returns 
  """
  return render_template('admin.html')

# Route handler for card
@app.route('/cards/<int:lesson_id>')
def show_card(lesson_id):
  """
  Creates a list of all cards for given lesson id
  :returns a list of cards
  """
  # Check if lesson exists
  lesson = db.session.query(Lesson).filter(Lesson.id == lesson_id).one_or_none()    
  if lesson is None:
    flash('Lesson Not Found') 
    return redirect(url_for('lessons'))     
  card_data = db.session.query(Card).filter(Card.lesson_id == lesson_id).all()
  # Check if the requested lesson has cards
  if len(card_data) == 0:
    flash('No Cards Available for the requested Lesson.') 
    return redirect(url_for('lessons'))    
  return render_template('cards.html', card_data=card_data)
  
  # card_data =  [
  #   {"id": 1,"card_name":"Lion","card_image":"lion.jpg","english_concept":"lion","hindi_concept":"शेर","lesson_id":1},
  #   {"id": 2,"card_name":"Zebra","card_image":"zebra.jpg","english_concept":"zebra","hindi_concept":"ज़ेबरा","lesson_id":1},
  #   {"id": 3,"card_name":"Monkey","card_image":"monkey.jpg","english_concept":"monkey","hindi_concept":"बंदर","lesson_id":1},
  #   {"id": 4,"card_name":"Cat","card_image":"cat.jpg","english_concept":"cat","hindi_concept":"बिल्ली","lesson_id":1},
  #   {"id": 5,"card_name":"Donkey","card_image":"donkey.jpg","english_concept":"donkey","hindi_concept":"गधा","lesson_id":1}
  # ]

  # card_data1 =  [
  #   {"id": 21,"card_name":"Tiger","card_image":"tiger.jpg","english_concept":"tiger","hindi_concept":"बाघ","lesson_id":5},
  #   {"id": 22,"card_name":"Horse","card_image":"horse.jpg","english_concept":"horse","hindi_concept":"घोड़ा","lesson_id":5},
  #   {"id": 23,"card_name":"Dog","card_image":"dog.jpg","english_concept":"dog","hindi_concept":"कुत्ता","lesson_id":5},
  #   {"id": 24,"card_name":"Elephant","card_image":"elephant.jpg","english_concept":"elephant","hindi_concept":"हाथी","lesson_id":5},
  #   {"id": 25,"card_name":"Panda","card_image":"panda.jpg","english_concept":"panda","hindi_concept":"पांडा","lesson_id":5}
  # ]


# Create Lesson
# -------------------

# Get the Create Lesson Form
"""
  Renders New Lesson Form
"""
@app.route('/lessons/create', methods=['GET'])
def create_lesson_form():
  form = LessonForm()
  return render_template('forms/new_lesson.html', form=form)

# Post handler for Lesson Creation
@app.route('/lessons/create', methods=['POST'])
def create_lesson_submission():
  """
    Add new lesson to database
    :return renders the lessons page
  """
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

# Edit Lesson

# reroute direct link to admin page
@app.route('/lessons/edit', methods=['GET'])
def lessson_edit_direct():
  """
    Redirects back to admin page
    which will ask for lesson id for editing    
  """
  return render_template('admin.html') 

# reroute to edit page for that lesson
@app.route('/lessons/edit', methods=['POST'])
def lessson_edit():
  """
    Gathers lesson info for lesson id to be edited
    and renders Edit Leson form
    :return requested lesson data for editing
  """
  try:
    lesson_id = request.form['lesson_id']
    lesson = db.session.query(Lesson).filter(Lesson.id == lesson_id).one_or_none()
    if lesson is None:
     abort(404)
    form = LessonForm()
    # set active place holders
    form.lesson_name.process_data(lesson.lesson_name)
    form.lesson_image.process_data(lesson.lesson_image)
    form.lesson_summary.process_data(lesson.lesson_summary)
    return render_template('forms/edit_lesson.html', form=form, lesson=lesson)
  except Exception:
    abort(422)

# direct edit lesson get route
@app.route('/lessons/<int:lesson_id>/edit', methods=['GET'])
def lessson_edit_get(lesson_id):
  """
    Gathers lesson info for lesson id to be edited
    and renders Edit Leson form
    :return requested lesson data for editing
  """
  try:
    lesson = db.session.query(Lesson).filter(Lesson.id == lesson_id).one_or_none()
    if lesson is None:
     abort(404)
    form = LessonForm()
    # set active place holders
    form.lesson_name.process_data(lesson.lesson_name)
    form.lesson_image.process_data(lesson.lesson_image)
    form.lesson_summary.process_data(lesson.lesson_summary)
    return render_template('forms/edit_lesson.html', form=form, lesson=lesson)
  except Exception:
    abort(422)
  
# Edit Lesson POST handler
@app.route('/lessons/<int:lesson_id>/edit', methods=['POST'])
def lessson_edit_submission(lesson_id):
  """
    Add edited lesson to database
    :return renders the lessons page
  """
  try:
    form = LessonForm()
    lesson = db.session.query(Lesson).filter(Lesson.id == lesson_id).first()
    # Updating values from form input    
    lesson.lesson_name = form.lesson_name.data
    lesson.lesson_image = form.lesson_image.data
    lesson.lesson_summary = form.lesson_summary.data
    db.session.commit()
    # on successful db insert, flash success
    flash('Lesson ' + request.form['lesson_name'] + ' was successfully updated!')
  except:
    db.session.rollback()
    flash('An error occured. Lesson ' + request.form['lesson_name'] + ' could not be updated!')
  finally:
    db.session.close()
  return redirect(url_for('lessons'))

# route handler for deleting a given Lesson
@app.route('/lessons/delete', methods=['POST'])
def lessson_delete():
  """
    Deletes lesson from database
    :return renders the lessons page
  """
  try:
    lesson_id = request.form['lesson_id']
    lesson = db.session.query(Lesson).filter(Lesson.id == lesson_id).one_or_none()
    if lesson is None:
     abort(404)    
    db.session.delete(lesson)
    db.session.commit()
    # on successful db delete, flash success
    flash('Lesson ' + lesson_id + ' was successfully deleted')    
  except:
    db.session.rollback()
    flash('An error occured. Lesson ' + lesson_id + ' could not be deleted')
  finally:
    db.session.close()
  return redirect(url_for('lessons'))

# Create Card
# -------------------

# Get the Create Card Form
@app.route('/cards/create', methods=['GET'])
def create_card_form():
  """
  Renders New Card Form
  """
  form = CardForm()
  return render_template('forms/new_card.html', form=form)

# Post handler for Card Creation
@app.route('/cards/create', methods=['POST'])
def create_card_submission():
  """
    Add new lesson to database
    :return renders the lessons page
  """
  try:
    form = CardForm()
    
    card_name = form.card_name.data
    card_image = form.card_image.data
    english_concept = form.english_concept.data
    hindi_concept = form.hindi_concept.data
    lesson_id = form.lesson_id.data
      
    card = Card(card_name=card_name,
    card_image=card_image,
    english_concept=english_concept,
    hindi_concept=hindi_concept,
    lesson_id=lesson_id
    )

    db.session.add(card)
    db.session.commit()
    # on successful db insert, flash success
    flash('Card ' + request.form['card_name'] + ' was successfully added.')
  except:
    db.session.rollback()
    flash('An error occured. Card ' + request.form['card_name'] + ' could not be added.')
  finally:
    db.session.close()
  return redirect(url_for('lessons'))

# Edit Card

# reroute direct link to admin page
@app.route('/cards/edit', methods=['GET'])
def card_edit_direct():
  """
    Redirects back to admin page
    which will ask for card id for editing    
  """
  return render_template('admin.html') 

# reroute to edit page for that card
@app.route('/cards/edit', methods=['POST'])
def card_edit():
  """
    Gathers card info for card id to be edited
    and renders Edit Card form
    :return requested card data for editing
  """
  try:
    card_id = request.form['card_id']
    card = db.session.query(Card).filter(Card.id == card_id).one_or_none()
    if card is None:
     abort(404)
    form = CardForm()
    # set active place holders
    form.card_name.process_data(card.card_name)
    form.card_image.process_data(card.card_image)
    form.english_concept.process_data(card.english_concept)
    form.hindi_concept.process_data(card.hindi_concept)
    form.lesson_id.process_data(card.lesson_id)    
    return render_template('forms/edit_card.html', form=form, card=card)
  except Exception:
    abort(422)

# direct edit card get route
@app.route('/cards/<int:card_id>/edit', methods=['GET'])
def card_edit_get(card_id):
  """
    Gathers card info for card id to be edited
    and renders Edit Card form
    :return requested card data for editing
  """
  try:
    card = db.session.query(Card).filter(Card.id == card_id).one_or_none()
    if card is None:
     abort(404)
    form = CardForm()
    # set active place holders
    form.card_name.process_data(card.card_name)
    form.card_image.process_data(card.card_image)
    form.english_concept.process_data(card.english_concept)
    form.hindi_concept.process_data(card.hindi_concept)
    form.lesson_id.process_data(card.lesson_id)    
    return render_template('forms/edit_card.html', form=form, card=card)
  except Exception:
    abort(422)

# Edit Card POST handler
@app.route('/cards/<int:card_id>/edit', methods=['POST'])
def card_edit_submission(card_id):
  """
    Add edited card to database
    :return renders the lessons page
  """
  try:
    form = CardForm()
    card = db.session.query(Card).filter(Card.id == card_id).first()
    # Updating values from form input    
    card.card_name = form.card_name.data
    card.card_image = form.card_image.data
    card.english_concept = form.english_concept.data
    card.hindi_concept = form.hindi_concept.data
    card.lesson_id = form.lesson_id.data
    db.session.commit()
    # on successful db insert, flash success
    flash('Card ' + request.form['card_name'] + ' was successfully updated!')
  except:
    db.session.rollback()
    flash('An error occured. Card ' + request.form['card_name'] + ' could not be updated!')
  finally:
    db.session.close()
  return redirect(url_for('lessons'))
  
# route handler for deleting a given card
@app.route('/cards/delete', methods=['POST'])
def card_delete():
  """
    Deletes lesson from database
    :return renders the lessons page
  """
  try:
    card_id = request.form['card_id']
    card = db.session.query(Card).filter(Card.id == card_id).one_or_none()
    if card is None:
     abort(404)    
    db.session.delete(card)
    db.session.commit()
    # on successful db delete, flash success
    flash('Card ' + card_id + ' was successfully deleted')    
  except:
    db.session.rollback()
    flash('An error occured. Card ' + card_id + ' could not be deleted')
  finally:
    db.session.close()
  return redirect(url_for('lessons'))

# Error Handler
@app.errorhandler(HTTPException)
def http_exception_handler(error):
  """
  HTTP error handler for all endpoints
  :param error: HTTPException containing code and description
  :return: error: HTTP status code, message: Error description
  """
  return jsonify({
      'success': False,
      'error': error.code,
      'message': error.description
  }), error.code

@app.errorhandler(Exception)
def exception_handler(error):
  """
  Generic error handler for all endpoints
  :param error: Any exception
  :return: error: HTTP status code, message: Error description
  """
  return jsonify({
      'success': False,
      'error': 500,
      'message': f'Something went wrong: {error}'
  }), 500
  