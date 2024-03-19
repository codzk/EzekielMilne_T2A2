from flask import Blueprint, request, jsonify
from datetime import timedelta
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token
from init import db, bcrypt
from models.user import User, user_schema

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route("/register", methods=["POST"])
def auth_register():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        # Input validation
        if not all((name, email, password)):
            return jsonify({"error": "Name, email, and password are required"}), 400

        # Check email format
        # Add your email format validation here
        
        # Check if email already exists
        if User.query.filter_by(email=email).first():
            return jsonify({"error": "Email address already in use"}), 409

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Create a new user
        user = User(name=name, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        return user_schema.dump(user), 201

    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Database error"}), 500

@auth_bp.route("/login", methods=["POST"])
def auth_login():
    try:
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        # Input validation
        if not all((email, password)):
            return jsonify({"error": "Email and password are required"}), 400

        # Query the database to find the user by email
        user = User.query.filter_by(email=email).first()

        # Check if user exists and password is correct
        if user and bcrypt.check_password_hash(user.password, password):
            # Create access token
            token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))
            return jsonify({"email": user.email, "token": token, "is_admin": user.is_admin}), 200
        else:
            return jsonify({"error": "Invalid email or password"}), 401

    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500
