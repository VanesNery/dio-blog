from http import HTTPStatus
from src.app import User, Role, db


def test_get_user_success(client):
   # Given
   role = Role(name='admin')
   db.session.add(role)
   db.session.commit()

   user = User(username='testuser', password='testpass', role_id=role.id)
   db.session.add(user)
   db.session.commit()

    # When
   response = client.get(f'/users/{user.id}')
   
    # Then
   assert response.status_code == HTTPStatus.OK
   assert response.json == {
       'id': user.id,
       'username': user.username,
       'password': user.password,
         'role': {
              'id': role.id,
              'name': role.name
         }
   }


def test_get_user_not_found(client):
    role = Role(name='admin')
    db.session.add(role)
    db.session.commit()

    user_id = 999  # Assuming this user ID does not exist in the database
    # When
    response = client.get(f'/users/{user_id}')  # Assuming user with ID 999 does not exist
    
    # Then
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_create_user_success(client, access_token):
    # Given
    role = db.session.execute(db.select(Role).where(Role.name == 'admin')).scalar()
    payload = {
        'username': 'newuser',
        'password': 'newpass',
        'role_id': role.id
    }

    # When
    response = client.post('/users/', json=payload, headers={'Authorization': f'Bearer {access_token}'})

    # Then
    assert response.status_code == HTTPStatus.CREATED
    assert response.json == {'message': 'Usuário criado com sucesso!'}
    assert db.session.execute(db.select(db.func.count(User.id))).scalar() == 2  # There should be 2 users in the database now


def test_list_users_success(client, access_token):
    # Given
    user = db.session.execute(db.select(User).where(User.username == 'testuser')).scalar()

    response = client.get('/users/', headers={'Authorization': f'Bearer {access_token}'})

    assert response.status_code == HTTPStatus.OK
    assert response.json == {
        'users': [
            {
                'id': user.id,
                'username': user.username,
                'password': user.password,
                'role_id': user.role_id
            }
        ]
    }


