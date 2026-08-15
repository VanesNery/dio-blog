from http import HTTPStatus

from flask import Blueprint, request
from src.models.models import db, Role

app = Blueprint('role', __name__, url_prefix='/roles')

@app.route('/', methods=['POST'])
def create_role():
    # Lógica para criar uma nova role
    data = request.json
    role = Role(name=data['name'])
    db.session.add(role)
    db.session.commit()
    return {'message': 'Role criada com sucesso!'}, HTTPStatus.CREATED


@app.route('/', methods=['GET'])
def list_roles():
    # Lógica para listar todas as roles
    query = db.select(Role)
    results = db.session.execute(query).scalars().all()
    return {'roles': [{'id': role.id, 'name': role.name} for role in results]}, HTTPStatus.OK
