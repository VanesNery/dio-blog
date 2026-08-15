from http import HTTPStatus

from flask import Blueprint, request
from src.models.post import Post
from src.models.base import db
from src.models.user import User
from sqlalchemy import inspect
from flask_jwt_extended import jwt_required, get_jwt_identity

app = Blueprint('post', __name__, url_prefix='/posts')

def _create_post():
    # Lógica para criar um novo post
    data = request.json
    post = Post(title=data['title'], body=data['body'], author_id=data['author_id'])
    db.session.add(post)
    db.session.commit()

def _list_posts():
    # Lógica para listar todos os posts
    query = db.select(Post)
    results = db.session.execute(query).scalars().all()
    return [{'id': post.id, 'title': post.title, 'body': post.body, 'author_id': post.author_id} for post in results]

@app.route('/', methods=['GET', 'POST'])
@jwt_required()
def handler_posts():
    user_id = get_jwt_identity()
    user = db.get_or_404(User, user_id)
    
    if not user.role or user.role.name != 'admin':
        if request.method == 'POST':
        # Lógica para criar um novo post
            _create_post()
            return {'message': 'Post criado com sucesso!'}, HTTPStatus.CREATED
    else:
        # Lógica para listar todos os posts
        return {'posts': _list_posts()}, HTTPStatus.OK

@app.route('/<int:post_id>')
def get_post(post_id):
    post = db.get_or_404(Post, post_id)
    return {'id': post.id, 'title': post.title, 'body': post.body, 'author_id': post.author_id}, HTTPStatus.OK

@app.route('/<int:post_id>', methods=['PATCH'])
@jwt_required()
def update_post(post_id):
    post = db.get_or_404(Post, post_id)
    data = request.json

    mapper = inspect(Post)
    for column in mapper.columns:
        if column.key in data:
            setattr(post, column.key, data[column.key])
    db.session.commit()
    return {'id': post.id, 'title': post.title, 'body': post.body, 'author_id': post.author_id}, HTTPStatus.OK
    
@app.route('/<int:post_id>', methods=['DELETE'])
@jwt_required()
def delete_post(post_id):
    post = db.get_or_404(Post, post_id)
    db.session.delete(post)
    db.session.commit()
    return {'message': 'Post deletado com sucesso!'}, HTTPStatus.OK
