from http import HTTPStatus

from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from src.models import db, User
from src.app import bcrypt

app = Blueprint('auth', __name__, url_prefix='/auth')


def _check_valid_password(password, hashed_password):
    return bcrypt.check_password_hash(hashed_password, password)


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username', None)
    password = data.get('password', None)
    user = db.session.execute(db.select(User).where(User.username == username)).scalar()
    # Lógica para autenticar o usuário (exemplo simplificado)
    if not user or not _check_valid_password(password, user.password):
        return {"message": "Bad username or password"}, HTTPStatus.UNAUTHORIZED
    
    access_token = create_access_token(identity=str(user.id))
    return {"access_token": access_token}, HTTPStatus.OK