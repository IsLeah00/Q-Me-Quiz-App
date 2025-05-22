from flask import Blueprint, render_template, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from better_profanity import profanity
from db import db
from models.question import Question
from models.answer import Answer
from models.topic import Topic
from models.user import User

create_quiz_bp = Blueprint('create_quiz', __name__)
profanity.load_censor_words()

@create_quiz_bp.route('/api/create-question', methods=['POST'])
@jwt_required()
def create_question():
    data = request.get_json()

    question_text = data.get("questionText")
    difficulty = data.get("difficulty")
    topic_names = data.get("topics")
    answers_data = data.get("answers")

    if not question_text or not difficulty or not topic_names or not answers_data:
        return jsonify({"error": "All fields are required"}), 400

    if len(topic_names) > 4:
        return jsonify({"error": "You can select up to 4 topics only."}), 400

    if len(answers_data) < 2 or len(answers_data) > 4:
        return jsonify({"error": "You must provide 2 to 4 answers"}), 400

    correct_answers = [a for a in answers_data if a.get("isCorrect")]
    if len(correct_answers) != 1:
        return jsonify({"error": "Exactly one answer must be marked correct"}), 400

    flagged = False
    censored_question = question_text
    censored_answers = []

    if profanity.contains_profanity(question_text):
        censored_question = profanity.censor(question_text)
        flagged = True

    for a in answers_data:
        answer_text = a["answerText"]
        censored = answer_text
        if profanity.contains_profanity(answer_text):
            censored = profanity.censor(answer_text)
            flagged = True
        censored_answers.append({
            "answerText": censored,
            "isCorrect": a["isCorrect"]
        })

    if flagged:
        return jsonify({
            "error": "Profanity detected. Please review your submission.",
            "censoredQuestion": censored_question,
            "censoredAnswers": censored_answers
        }), 400

    topics = []
    for name in topic_names:
        topic = Topic.query.filter_by(topicName=name).first()
        if not topic:
            return jsonify({"error": f"Topic '{name}' not found"}), 404
        topics.append(topic)

    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    new_question = Question(
        questionText=question_text,
        difficulty=difficulty,
        userId=user.userId
    )

    new_question.topics = topics

    db.session.add(new_question)
    db.session.flush()

    for a in answers_data:
        answer = Answer(
            answerText=a["answerText"],
            isCorrect=a["isCorrect"],
            question=new_question
        )
        db.session.add(answer)

    db.session.commit()

    return jsonify({"message": "Question created successfully!"}), 201


@create_quiz_bp.route('/get-creative', methods=['GET'])
@jwt_required()
def quiz_create_page():
    topics = Topic.query.all()
    return render_template("get-creative.html", topics=topics)
