from flask import request
from flask_restplus import Resource

from ..util.dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_a_user

from ..util.decorator import admin_token_required, token_required


api = UserDto.api
_user = UserDto.user

# create a parser for handling Authorization headers
parser = api.parser()
parser.add_argument('Authorization', location='headers')


@api.route('/')
@api.response(201, 'User successfully created')
@api.response(409, 'User already exists. Please Log in')
@api.expect(_user, validate=True)
class createUser(Resource):
    
    def post(self):
        '''Creates a new User'''
        data = request.json
        return save_new_user(data=data)


@api.route('/all')
@api.response(200, 'Success')
class UserList(Resource):

    @api.marshal_list_with(_user, envelope='data')
    @api.expect(parser)
    @token_required
    @admin_token_required
    def get(self):
        '''Admin view all registered users'''
        return get_all_users()


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found')
class User(Resource):
    @api.marshal_with(_user)
    @api.expect(parser)
    @token_required
    @admin_token_required
    def get(self, public_id):
        '''Admin user lookup'''
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user


@api.route('/test')
class Test(Resource):

    @api.expect(parser)
    @token_required
    def get(self):
        re = {
            'status': 'How did you get here',
            'message': 'LEAVE'
        }
