import json
import os
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash
from models.user import User
from models.topic import Topic
from models.question import Question
from models.answer import Answer
from models.result import Result
from models.leaderboard import LeaderBoard
from db import db

def load_initial_data():
    try:
        data_path = os.path.join(os.path.dirname(__file__), "..", "data")

        load_users(data_path)
        load_topics(data_path)
        load_questions(data_path)
        load_results(data_path)

        print("Initial data loaded successfully")

    except Exception as e:
        print(f"Failed to load initial data: {e}")


def load_users(data_path):
    with open(os.path.join(data_path, "user.json")) as f:
        users = json.load(f)
        for user_data in users:
            hashed_pw = generate_password_hash(user_data["password"])
            new_user = User(
                username=user_data["username"],
                birthdate=user_data["birthdate"],
                passwordHash=hashed_pw,
                profilePic=user_data.get("profilePic"),
                rank=0,
                score=0
            )
            db.session.add(new_user)
        db.session.commit()


def load_topics(data_path):
    with open(os.path.join(data_path, "topics.json")) as f:
        for t in json.load(f):
            db.session.add(Topic(topicName=t["topicName"]))
        db.session.commit()


def load_questions(data_path):
    with open(os.path.join(data_path, "questions.json")) as f:
        for q_data in json.load(f):
            question = Question(
                questionText=q_data["questionText"],
                difficulty=q_data["difficulty"],
                userId=q_data.get("userId")
            )
            topic = Topic.query.filter_by(topicName=q_data["topicName"]).first()
            if topic:
                question.topics.append(topic)

            db.session.add(question)
            db.session.flush()

            for ans in q_data["answers"]:
                db.session.add(Answer(
                    answerText=ans["answerText"],
                    isCorrect=ans["isCorrect"],
                    questionId=question.questionId
                ))
        db.session.commit()


def load_results(data_path):
    with open(os.path.join(data_path, "results.json")) as f:
        for r_data in json.load(f):
            user = User.query.filter_by(username=r_data["username"]).first()
            if not user:
                continue

            total = 0
            top = 0

            for result in r_data["results"]:
                topic = Topic.query.filter_by(topicName=result["topic"]).first()
                if not topic or not topic.questions:
                    continue

                valid_questions = topic.questions[:5]
                correct_answers = [
                    a for q in valid_questions for a in q.answers if a.isCorrect
                ][:result["score"]]

                score = result["score"]
                multiplier = result["multiplier"]
                final_score = score * multiplier
                total += final_score
                top = max(top, final_score)

                res = Result(
                    score=score,
                    difficultyMultiplier=multiplier,
                    user=user,
                    updatedAt=datetime.now(timezone.utc)
                )

                res.questions = valid_questions
                res.answers = correct_answers

                db.session.add(res)

            user.score = total
            existing = LeaderBoard.query.filter_by(userId=user.userId).first()
            if existing:
                existing.totalScore = total
                existing.topScore = top
                existing.updatedAt = datetime.now(timezone.utc)
            else:
                db.session.add(LeaderBoard(
                    userId=user.userId,
                    totalScore=total,
                    topScore=top,
                    updatedAt=datetime.now(timezone.utc)
                ))

        db.session.commit()
