from flask_wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, URL
import os

#https://stackoverflow.com/questions/29169699/flask-wtforms-populating-drop-down-list
#Image Files
imagefilenames = os.listdir("static/img")

class LessonForm(Form):
  lesson_name = StringField(
        u'Lesson Name', validators=[DataRequired()]
  )
  lesson_image = SelectField(
        u'Lesson Image', validators=[DataRequired()], choices=[(f, f) for f in imagefilenames]
  )
  lesson_summary = StringField(
        u'Lesson Summary', validators=[DataRequired()]
  )

  class CardForm(Form):
  card_name = StringField(
        u'Card Name', validators=[DataRequired()]
  )
  card_image = SelectField(
        u'Card Image', validators=[DataRequired()], choices=[(f, f) for f in imagefilenames]
  )
  english_concept = StringField(
        u'English Concept', validators=[DataRequired()]
  )
  hindi_concept = StringField(
        u'Hindi Summary', validators=[DataRequired()]
  )
  lesson_id = StringField(
        'Lesson Id', validators=[DataRequired()]
    )
  