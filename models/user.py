from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from db import db

class User(db.Model):
    __tablename__ = 'users'

    userId = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    rank = db.Column(db.Integer, default=0)
    score = db.Column(db.Integer, default=0)
    passwordHash = db.Column(db.String(200), nullable=False)
    profilePic = db.Column(db.String(255), nullable=True)

    results = db.relationship('Result', backref='user', lazy=True)
    leaderboard_entries = db.relationship('LeaderBoard', backref='user', lazy=True)
    questions = db.relationship('Question', backref='creator', lazy=True)
