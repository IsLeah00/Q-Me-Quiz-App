from flask import Blueprint, render_template, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from db import db
from models.question import Question
from models.answer import Answer
from models.result import Result
from models.topic import Topic
from models.user import User
from models.leaderboard import LeaderBoard
from datetime import datetime, timezone
import random

quiz_bp = Blueprint('quiz', __name__)

DIFFICULTY_MULTIPLIERS = {
    'easy': 1,
    'medium': 2,
    'hard': 3
}


@quiz_bp.route('/api/start-quiz', methods=['POST'])
@jwt_required()
def start_quiz():
    data = request.get_json()
    difficulty = data.get('difficulty')
    topic_name = data.get('topic')

    if not difficulty or not topic_name:
        return jsonify({"error": "Please provide difficulty and topic"}), 400

    topic = Topic.query.filter_by(topicName=topic_name).first()
    if not topic:
        return jsonify({"error": "Topic not found"}), 404

    valid_questions = [q for q in topic.questions if q.difficulty == difficulty and 2 <= len(q.answers) <= 5]

    if len(valid_questions) < 5:
        return jsonify({"error": "This quiz is not ready for use yet..."}), 400

    selected_questions = random.sample(valid_questions, 5)

    quiz = []
    for question in selected_questions:
        quiz.append({
            "questionId": question.questionId,
            "questionText": question.questionText,
            "answers": [
                {"answerId": ans.answerId, "answerText": ans.answerText}
                for ans in question.answers
            ]
        })

    return jsonify({"quiz": quiz}), 200


@quiz_bp.route('/api/submit-quiz', methods=['POST'])
@jwt_required()
def submit_quiz():
    data = request.get_json()
    submitted = data.get('answers')
    difficulty = data.get('difficulty')
    topic_name = data.get('topic')

    if not submitted or not difficulty or not topic_name:
        return jsonify({"error": "Missing data"}), 400

    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    topic = Topic.query.filter_by(topicName=topic_name).first()

    score = 0
    correct_count = 0
    multiplier = DIFFICULTY_MULTIPLIERS.get(difficulty, 1)

    selected_answers = []
    selected_questions = []

    for item in submitted:
        question_id = item.get('questionId')
        answer_id = item.get('answerId')

        question = Question.query.get(question_id)
        answer = Answer.query.get(answer_id)

        if question and answer and answer.questionId == question_id:
            selected_questions.append(question)
            selected_answers.append(answer)
            if answer.isCorrect:
                correct_count += 1
                score += 1 * multiplier

    result = Result(
        score=score,
        difficultyMultiplier=multiplier,
        user=user
    )

    result.questions = selected_questions
    result.answers = selected_answers
    db.session.add(result)

    entry = LeaderBoard.query.filter_by(userId=user_id).first()
    if entry:
        entry.totalScore += score
        entry.topScore = max(entry.topScore, score)
        entry.updatedAt = datetime.now(timezone.utc)
    else:
        new_entry = LeaderBoard(
            userId=user_id,
            totalScore=score,
            topScore=score,
            updatedAt=datetime.now(timezone.utc)
        )
        db.session.add(new_entry)

    db.session.commit()

    return jsonify({
        "correct": correct_count,
        "total": 5,
        "score": score,
        "multiplier": multiplier
    }), 200


@quiz_bp.route("/home", methods=["GET"])
@jwt_required()
def home_page():
    topics = Topic.query.all()
    return render_template("home.html", topics=topics)
