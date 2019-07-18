import uuid
import datetime

from .. import db
from ..model.user import User


def save_new_user(data):
    email = User.query.filter_by(email=data['email']).first()
    username = User.query.filter_by(username=data['username']).first()
    if not email and not username:
        if data['admin']:
            new_user = User(
                public_id=(str(uuid.uuid4())),
                email=data['email'],
                username=data['username'],
                password=data['password'],
                registered_on=datetime.datetime.utcnow(),
                admin=data['admin']
            )
        else:
            new_user = User(
                public_id=(str(uuid.uuid4())),
                email=data['email'],
                username=data['username'],
                password=data['password'],
                registered_on=datetime.datetime.utcnow(),
                admin=data['admin']
            )

        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return generate_token(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()


def generate_token(user):
    try:
        auth_token = user.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. please try again'
        }
        return response_object, 401
