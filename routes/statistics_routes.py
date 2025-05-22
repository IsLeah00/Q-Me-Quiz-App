from flask import Blueprint, jsonify, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity
from db import db
from models.result import Result
from models.user import User
from models.topic import Topic
from datetime import datetime
from collections import defaultdict

statistics_bp = Blueprint('statistics', __name__)


@statistics_bp.route('/api/user-statistics', methods=['GET'])
@jwt_required()
def user_statistics():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    topic_stats = defaultdict(lambda: {"total": 0, "correct": 0})

    for result in user.results:
        for question in result.questions:
            for topic in question.topics:
                topic_stats[topic.topicName]["total"] += 1
                for answer in result.answers:
                    if answer.questionId == question.questionId and answer.isCorrect:
                        topic_stats[topic.topicName]["correct"] += 1

    response = []
    for topic, stats in topic_stats.items():
        correct_rate = (stats["correct"] / stats["total"]) * 100 if stats["total"] > 0 else 0
        response.append({
            "topic": topic,
            "averageCorrectAnswerRate": round(correct_rate, 2)
        })

    return jsonify(response), 200


@statistics_bp.route('/api/global-statistics', methods=['GET'])
def global_statistics():
    user_scores = defaultdict(lambda: {"totalScore": 0, "count": 0})

    all_users = User.query.all()
    now = datetime.now().date()

    for user in all_users:
        age = (now - user.birthdate).days // 365
        for result in user.results:
            user_scores[age]["totalScore"] += result.score
            user_scores[age]["count"] += 1

    response = []
    for age, stats in sorted(user_scores.items()):
        avg_score = stats["totalScore"] / stats["count"] if stats["count"] > 0 else 0
        response.append({
            "age": age,
            "ageCorrectAnswerRate": round(avg_score, 2)
        })

    return jsonify(response), 200


@statistics_bp.route("/statistics", methods=["GET"])
@jwt_required()
def statistics_page():
    return render_template("statistics.html")
