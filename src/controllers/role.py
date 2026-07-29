from http import HTTPStatus

from flask import Blueprint, request
from src.app import db, Role

app = Blueprint('role', __name__, url_prefix='/roles')

@app.route('/', methods=['POST'])
def create_role():
    # Lógica para criar uma nova role
    data = request.json
    role = Role(name=data['name'])
    db.session.add(role)
    db.session.commit()
    return {'message': 'Role criada com sucesso!'}, HTTPStatus.CREATED