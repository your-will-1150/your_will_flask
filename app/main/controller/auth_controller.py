from flask import request
from flask_restplus import Resource

from app.main.service.auth_helper import Auth
from ..util.dto import AuthDto
from ..util.decorator import Authenticate

api = AuthDto.api
user_auth = AuthDto.user_auth


@api.route('/login')
class UserLogin(Resource):
    '''User Login resource'''
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        post_data = request.json
        print(post_data)
        return Auth.login_user(data=post_data)


@api.route('/logout')
class LogoutAPI(Resource):
    '''Logout Resource'''
    @Authenticate
    @api.doc('Logout a user')
    def post(self):
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(data=auth_header)


@api.route('/delete')
class DeleteUser(Resource):
    ''' Delete user'''
    @api.doc('Delete User')
    def post(self):
        data = request.json
        auth_token = request.headers.get('Authorization')
        return Auth.delete_user(data, auth_token)
