from http import HTTPStatus

from flask import Blueprint, request
from src.models import db, User
from sqlalchemy import inspect
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.utils import requires_role
from src.app import bcrypt
from src.views.user import CreateUserSchema, UserSchema
from marshmallow import ValidationError

app = Blueprint('user', __name__, url_prefix='/users')

def _create_user():
    # Lógica para criar um novo usuário
    user_schema = CreateUserSchema()

    try:
        data = user_schema.load(request.json)
    except ValidationError as err:
        return {'errors': err.messages}, HTTPStatus.UNPROCESSABLE_ENTITY

    user = User(
        username=data['username'], 
        password=bcrypt.generate_password_hash(data['password']), 
        role_id=data['role_id']
    )
    db.session.add(user)
    db.session.commit()
    return {'message': 'Usuário criado com sucesso!'}, HTTPStatus.CREATED


@jwt_required()
@requires_role('admin')
def _list_users():
    # Lógica para listar todos os usuários
    user_id = get_jwt_identity()
    user = db.get_or_404(User, user_id)
    query = db.select(User)
    users = db.session.execute(query).scalars()
    users_schema = UserSchema(many=True)
    return users_schema.dump(users)


@app.route('/', methods=['GET', 'POST'])
def list_or_create_users():

    if request.method == 'POST':
        # Lógica para criar um novo usuário
        _create_user()


    # if not user.role or user.role.name != 'admin':
    #     return {'message': 'Acesso negado. Apenas administradores podem acessar esta rota.'}, HTTPStatus.FORBIDDEN

    # Lógica para listar todos os usuários
    return {'users': _list_users()}, HTTPStatus.OK

@app.route('/<int:user_id>')
def get_user(user_id):
    # Lógica para obter um usuário específico pelo ID
    user = db.get_or_404(User, user_id)
    return {'id': user.id, 'username': user.username, 'password': user.password, 'role':{
        'id': user.role.id, 'name': user.role.name
    }}, HTTPStatus.OK

@app.route('/<int:user_id>', methods=['PATCH'])
@requires_role('admin')
def update_user(user_id):
    # Lógica para atualizar um usuário específico pelo ID
    user = db.get_or_404(User, user_id)
    data = request.json

    mapper = inspect(User)
    for column in mapper.columns:
        if column.key in data:
            setattr(user, column.key, data[column.key])
    db.session.commit()

    return {'id': user.id, 'username': user.username}, HTTPStatus.OK

@app.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
@requires_role('admin')
def delete_user(user_id):
    # Lógica para deletar um usuário específico pelo ID
    user = db.get_or_404(User, user_id)
    db.session.delete(user)
    db.session.commit()
    return {'message': 'Usuário deletado com sucesso!'}, HTTPStatus.NO_CONTENT
