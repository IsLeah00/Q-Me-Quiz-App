from datetime import datetime, timezone
from db import db

class LeaderBoard(db.Model):
    __tablename__ = 'leaderboard'

    rankId = db.Column(db.Integer, primary_key=True)
    topScore = db.Column(db.Integer, nullable=False)
    totalScore = db.Column(db.Integer, nullable=False)
    updatedAt = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    userId = db.Column(db.Integer, db.ForeignKey('users.userId'), nullable=False)
