

from flask import Blueprint, request
from server.models.user import User
from server.app import db
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return {'error': 'Username already exists'}, 400

    user = User(username=username)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return {'message': 'User registered successfully'}, 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        token = create_access_token(identity=user.id)
        return {'token': token}, 200

    return {'error': 'Invalid credentials'}, 401
