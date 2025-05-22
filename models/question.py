from db import db
from .answer import Answer
from .statistics import Statistics
from .result import result_questions

question_topics = db.Table('question_topics',
    db.Column('questionId', db.Integer, db.ForeignKey('questions.questionId'), primary_key=True),
    db.Column('topicId', db.Integer, db.ForeignKey('topics.topicId'), primary_key=True)
)

class Question(db.Model):
    __tablename__ = 'questions'

    questionId = db.Column(db.Integer, primary_key=True)
    questionText = db.Column(db.Text, nullable=False)
    difficulty = db.Column(db.String(10), nullable=False)

    userId = db.Column(db.Integer, db.ForeignKey('users.userId'), nullable=True)
    
    answers = db.relationship('Answer', backref='question', lazy=True)
    topics = db.relationship('Topic', secondary=question_topics, back_populates='questions', lazy=True)
    statistics = db.relationship('Statistics', backref='question', lazy=True)
    results = db.relationship('Result', secondary=result_questions, back_populates='questions', lazy=True)
