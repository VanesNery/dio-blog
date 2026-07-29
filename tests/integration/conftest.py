import pytest
from src.app import Role, User, create_app, db

@pytest.fixture()
def app():
    app = create_app({
        "SECRET_KEY": "test",
        "SQLALCHEMY_DATABASE_URI": "sqlite://",
        "JWT_SECRET_KEY": "test",
    })
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture()
def access_token(client):
    role = Role(name='admin')
    db.session.add(role)
    db.session.commit()

    user = User(username='testuser', password='testpass', role_id=role.id)
    db.session.add(user)
    db.session.commit()

    access_token = client.post('/auth/login', json={'username': user.username, 'password': user.password}).json['access_token']
    return access_token

@pytest.fixture()
def client(app):
    return app.test_client()
