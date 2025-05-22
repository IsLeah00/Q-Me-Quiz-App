from db import db
from .result import result_answers

class Answer(db.Model):
    __tablename__ = 'answers'

    answerId = db.Column(db.Integer, primary_key=True)
    answerText = db.Column(db.Text, nullable=False)
    isCorrect = db.Column(db.Boolean, nullable=False)
    answerSubmitSum = db.Column(db.Integer, default=0)

    questionId = db.Column(db.Integer, db.ForeignKey('questions.questionId'), nullable=False)
    results = db.relationship('Result', secondary=result_answers, back_populates='answers', lazy=True)
