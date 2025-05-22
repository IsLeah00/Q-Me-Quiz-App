from db import db

class Statistics(db.Model):
    __tablename__ = 'statistics'

    statId = db.Column(db.Integer, primary_key=True)
    ageCorrectAnswerRate = db.Column(db.Float, nullable=False)
    averageCorrectAnswerRate = db.Column(db.Float, nullable=False)

    topicId = db.Column(db.Integer, db.ForeignKey('topics.topicId'), nullable=False)
    questionId = db.Column(db.Integer, db.ForeignKey('questions.questionId'), nullable=True)
