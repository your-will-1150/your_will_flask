import uuid
from datetime import datetime
from .. import db
from ..model.user import User
import re
from ..util import dto




def create_user(data):
    user = User.query.filter_by(email=data['email']).first()

    if not _check_password_requirements(data.get('password')):
        return {
            'status' : 'fail',
            'message' : 'Weak password, must include an Uppercase, lowercase, one or more of @$!%*#?&, and be 6-20 letters long'
        }

    if not user:
        new_user = User(
            public_id=uuid.uuid4(),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.utcnow(),
            admin=False
        )
        
        if new_user.username == 'username':
            new_user.admin = True
                  
            
            save_changes(new_user)
            response_object = {
                'status': 'success',
                'message': 'Successfully registered.'
            }
            return generate_token(new_user)
        else:
            print('failed')
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

def _check_password_requirements(password):
    pattern = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$')
    match = re.search(pattern, password)

    if match:
        return True
    
# make sure to change this in other files
def get_all_users():
    return User.query.all()


def get_a_user(id):
    return User.query.filter_by(id=id).first()

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

#admin function
def delete_by_id(id, public_id):
    real_dat = User.query.filter_by(id=id).first()
    user_del = User.query.filter_by(public_id=public_id).first()
    if real_dat.admin:
        db.session.delete(user_del)
        db.session.commit()
        return None, 204
    else:
        response = {'status' : 'failed, not an admin'}
        return response


#admin function
def update_by_id(id, data, public_id):
    real_dat = User.query.filter_by(id=id).first()
    if real_dat.admin:
        user = get_a_user(public_id)
        for key, item in data.items():
            setattr(user, key, item)
        user.modified_at = datetime.utcnow()
        if not _check_password_requirements(data.get('password')):
            return {
                'status' : 'fail',
                'message' : 'Weak password, must include an Uppercase, lowercase, one or more of @$!%*#?&, and be 6-20 letters long'
            }
        db.session.commit()
        response = {'status' : 'updated user'}
        return response, 200
    else:
        response = {'status' : 'failed, not an admin'}
        return response

def save_changes(data):
    db.session.add(data)
    db.session.commit()

def update_user(id, data):
    user = get_a_user(id)
    for key, item in data.items():
        setattr(user, key, item)
    user.modified_at = datetime.utcnow()
    if not _check_password_requirements(data.get('password')):
        return {
            'status' : 'fail',
            'message' : 'Weak password, must include an Uppercase, lowercase, one or more of @$!%*#?&, and be 6-20 letters long'
        }
    db.session.commit()
    response = {'status' : 'updated user'}
    return response, 200

def delete_user(id):
    user2 = get_a_user(id)
    # user = User.query.filter_by(public_id=id).first()
    db.session.delete(user2)
    db.session.commit()
    return None, 204

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

def grant_admin_status(id):
    real_dat = User.query.filter_by(id=id).first()
    if real_dat.admin:
        pass
        
