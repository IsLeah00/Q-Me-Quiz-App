from flask import Blueprint, jsonify, make_response, redirect, render_template, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from db import db
from models.user import User
from flask_jwt_extended import create_access_token, set_access_cookies, unset_jwt_cookies
from datetime import datetime, timezone
import re
import os

auth_bp = Blueprint('auth', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'svg'}

def allowed_file(profileFilename):
    return '.' in profileFilename and profileFilename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@auth_bp.route('/api/register', methods=['POST'])
def register():
    data = request.form
    file = request.files.get('profilePic')

    username = data.get('username')
    birthdate = data.get('birthdate')
    password = data.get('password')

    if not username or not birthdate or not password:
        return jsonify({"error": "All required fields must be provided!"}), 400

    try:
        birth = datetime.strptime(birthdate, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        age = (datetime.now(timezone.utc) - birth).days // 365
        if age < 16:
            return jsonify({"error": "You must be at least 16 years old to register!"}), 400
    except ValueError:
        return jsonify({"error": "Invalid birthdate format!"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists!"}), 400

    if len(password) < 6 or not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password) \
            or not re.search(r'[0-9]', password) or not re.search(r'[\W_]', password):
        return jsonify({"error": "Password must pass all requirements!"}), 400

    profileFilename = None
    os.makedirs("static/images/profiles", exist_ok=True)

    if file and allowed_file(file.filename):
        ext = file.filename.rsplit('.', 1)[1].lower()
        profileFilename = f"{username}.{ext}"
        path = os.path.join("static/images/profiles", profileFilename)
        file.save(path)
    elif file:
        return jsonify({"error": "Unsupported file type!"}), 400

    new_user = User(
        username=username,
        birthdate=birth,
        passwordHash=generate_password_hash(password),
        profilePic=profileFilename,
        rank=0,
        score=0
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Registration successful!\nRedirecting to login..."}), 201

@auth_bp.route('/api/login', methods=['POST'])
def login():
    data = request.form
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.passwordHash, password):
        return jsonify({"error": "Invalid username or password!"}), 401

    token = create_access_token(identity=user.userId)
    resp = make_response(jsonify({"message": "Login successful!"}))
    set_access_cookies(resp, token)
    return resp


@auth_bp.route("/api/logout", methods=["POST"])
def logout():
    resp = make_response(redirect(url_for("auth.login_page")))
    unset_jwt_cookies(resp)
    return resp


@auth_bp.route("/register", methods=["GET"])
def register_page():
    return render_template("register.html")


@auth_bp.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")


@auth_bp.route("/logout", methods=["GET"])
def logout_page():
    return render_template("logout.html")
