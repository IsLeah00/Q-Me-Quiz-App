from flask import Blueprint, jsonify, render_template, request
from flask_jwt_extended import jwt_required
from models.leaderboard import LeaderBoard
from models.user import User
from datetime import datetime

leaderboard_bp = Blueprint('leaderboard', __name__)

@leaderboard_bp.route('/api/leaderboard', methods=['GET'])
def get_leaderboard():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get("limit", 5))

    query = LeaderBoard.query.join(User).order_by(LeaderBoard.totalScore.desc())
    total_entries = query.count()
    total_pages = (total_entries - 1) // limit + 1

    entries = query.offset((page - 1) * limit).limit(limit).all()

    if not entries:
        return jsonify({"error": "No leaderboard entries found"}), 404

    top_entry = LeaderBoard.query.join(User).order_by(LeaderBoard.totalScore.desc()).first()

    def serialize(entry):
        return {
            "username": entry.user.username,
            "profilePic": entry.user.profilePic,
            "totalScore": entry.totalScore,
            "topScore": entry.topScore,
            "updatedAt": (entry.updatedAt or datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
        }

    return jsonify({
        "topUser": serialize(top_entry),
        "others": [serialize(e) for e in entries if e != top_entry],
        "currentPage": page,
        "totalPages": total_pages,
        "hasNext": page < total_pages,
        "hasPrev": page > 1
    }), 200


@leaderboard_bp.route('/leaderboard', methods=['GET'])
@jwt_required()
def leaderboard_page():
    return render_template("leaderboard.html")
