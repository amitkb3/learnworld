from app import db

# tip: cascade delete
# : https://stackoverflow.com/questions/5033547/sqlalchemy-cascade-delete
# for cascade to work need to modify Foreign key and relationship statements

# --------------------
# Models.
# --------------------


class Lesson(db.Model):
    __tablename__ = 'lessons'

    id = db.Column(db.Integer, primary_key=True)
    lesson_name = db.Column(db.String(50), nullable=False)
    lesson_image = db.Column(db.String(500))
    lesson_summary = db.Column(db.String(100))
    cards = db.relationship('Card', backref='lesson',
                            lazy=True, passive_deletes=True)

    def __repr__(self):
        return 'Lesson id: {} name: {}'.format(self.id, self.lesson_name)


class Card(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    card_name = db.Column(db.String(50), nullable=False)
    card_image = db.Column(db.String(500))
    english_concept = db.Column(db.String(50), nullable=False)
    hindi_concept = db.Column(db.String(50), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey(
        'lessons.id', ondelete='CASCADE'), nullable=False)

    def __repr__(self):
        return 'Card id: {} name: {}'.format(self.id, self.card_name)
