from db import db
from .question import question_topics

class Topic(db.Model):
    __tablename__ = 'topics'

    topicId = db.Column(db.Integer, primary_key=True)
    topicName = db.Column(db.String(100), nullable=False, unique=True)

    questions = db.relationship('Question', secondary=question_topics, back_populates='topics', lazy=True)
    statistics = db.relationship('Statistics', backref='topic', lazy=True)
