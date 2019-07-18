from functools import wraps
from flask import request

from app.main.service.auth_helper import Auth

from .dto import UserDto

api = UserDto.api


@api.response(401, 'You must be logged in to access')
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        try:
            data, status = Auth.get_logged_in_user(request)
            token = data.get('data')
        except Exception as e:
            response_object = {
                'status': 'Failed',
                'message': 'You must be logged in to access'
            }
            return response_object, 401

        if not token:
            response_object = {
                'status': 'Failed',
                'message': 'You must be logged in to access'
            }
            return response_object, 401

    return decorated


@api.response(401, 'Admin token required')
def admin_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        try:
            data, status = Auth.get_logged_in_user(request)
            token = data.get('data')
        except Exception as e:
            response_object = {
                'status': 'Failed',
                'message': 'You must be an Admin to access'
            }
            return response_object, 401

        if not token:
            return data, status

        admin = token.get('admin')
        if not admin:
            response_object = {
                'status': 'fail',
                'message': 'You must be an Admin to access'
            }
            return response_object, 401
        return f(*args, **kwargs)

    return decorated
