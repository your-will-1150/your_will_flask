from functools import wraps
from flask import request, g

from app.main.service.auth_helper import Auth

from .dto import UserDto

api = UserDto.api


def Authenticate(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        

        token = data.get('data')
        if not token:
            return data, status
        
        g.user = {'owner_id' : data['data']['user_id']}
        print(g.user)
        return f(*args, **kwargs)

    return decorated

def AdminAuthenticate(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status
        
        admin = token.get('admin')
        if not admin:
            response_object = {
                'status' : 'fail',
                'message' : 'admin_token_required'
            }
            return response_object, 401
        
        return f(*args, **kwargs)
    
    return decorated