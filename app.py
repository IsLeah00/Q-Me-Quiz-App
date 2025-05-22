from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config
from services.guest_guard import check_guest_access
from services.auth_guard import check_auth_access
from services.seed_data import load_initial_data
from db import db
from routes.auth_routes import auth_bp
from routes.quiz_routes import quiz_bp
from routes.create_quiz_routes import create_quiz_bp
from routes.statistics_routes import statistics_bp
from routes.leaderboard_routes import leaderboard_bp


jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)
    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(quiz_bp)
    app.register_blueprint(create_quiz_bp)
    app.register_blueprint(statistics_bp)
    app.register_blueprint(leaderboard_bp)

    @app.before_request
    def apply_guards():
        auth_redirect = check_auth_access()
        if auth_redirect:
            return auth_redirect

        guest_redirect = check_guest_access()
        if guest_redirect:
            return guest_redirect

    return app

def test_db_connection(app):
    try:
        with app.app_context():
            print("Database URI:", app.config["SQLALCHEMY_DATABASE_URI"])

            from models import (
                User, Topic, Question, Answer,
                Result, LeaderBoard, Statistics
            )

            print("Reset database...")
            db.drop_all()
            print("Creating tables now...")
            db.create_all()
            print("All tables created!")
            load_initial_data()

    except Exception as e:
        print("Failed to connect to MySQL database...")
        print(f"Error: {e}")

if __name__ == "__main__":
    app = create_app()
    test_db_connection(app)
    print("Server running on http://localhost:8080...")
    app.run(debug=False, use_reloader=False, port=8080)
