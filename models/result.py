from datetime import datetime, timezone
from db import db

result_questions = db.Table('result_questions',
    db.Column('resultId', db.Integer, db.ForeignKey('results.resultId'), primary_key=True),
    db.Column('questionId', db.Integer, db.ForeignKey('questions.questionId'), primary_key=True)
)

result_answers = db.Table('result_answers',
    db.Column('resultId', db.Integer, db.ForeignKey('results.resultId'), primary_key=True),
    db.Column('answerId', db.Integer, db.ForeignKey('answers.answerId'), primary_key=True)
)

class Result(db.Model):
    __tablename__ = 'results'

    resultId = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, nullable=False)
    difficultyMultiplier = db.Column(db.Integer, nullable=False)
    updatedAt = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    userId = db.Column(db.Integer, db.ForeignKey('users.userId'), nullable=False)

    questions = db.relationship('Question', secondary=result_questions, back_populates='results', lazy=True)
    answers = db.relationship('Answer', secondary=result_answers, back_populates='results', lazy=True)
