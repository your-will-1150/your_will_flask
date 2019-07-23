from flask import request, g
from flask_restplus import Resource

from ..util.dto import UserDto, UserCreateDto, UserDetailDto, UserUpdateDto, UserMe
from ..service import user_service
from ..util.decorator import Authenticate



api = UserDto.api
user = UserDto.user
user_create = UserCreateDto.user
user_detail = UserDetailDto.user
user_update = UserUpdateDto.user
user_me = UserMe.user

parser = api.parser()
parser.add_argument('Authorization', location='headers')


# @api.route('/')
# class UserCreate(Resource):
#     @api.response(201, 'User successfully created')
#     @api.doc('create new user')
#     @api.response(409, 'User already exists. Please Log in')
#     @api.expect(user, validate=True)
#     def post(self):
#         '''Creates a new User'''
#         data = request.json
#         return user_service.save_new_user(data=data)


@api.route('/all')
@api.response(200, 'Success')
class UserList(Resource):
    
    @api.response(201, 'User created')
    @api.doc('create a new user')
    @api.expect(user_create, validate=True)
    def post(self):
        data = request.json
        return user_service.create_user(data=data)

# @api.route('/<public_id>')
# class User(Resource):

#     @api.response(404, 'user not found')
#     @api.doc('get a user')
#     @api.marshal_with(user_detail)
#     def get(self, id):
#         '''Admin user lookup'''
#         return user_service.get_a_user(id)


# # @api.route('/test')
# # class Test(Resource):

# #     @api.expect(parser)
# #     @token_required
# #     def get(self):
# #         re = {
# #             'status': 'How did you get here',
# #             'message': 'LEAVE'
#         }


@api.route('/me')
@api.response(401, 'unauthorized')
@api.expect(parser)
class UserMe(Resource):

    @api.doc('update users account')
    @api.expect(user_update)
    @Authenticate
    def put(self):
        data = request.json
        user_id = g.user.get('owner_id')
        return user_service.update_user(user_id, data)

    @api.doc('get account associated with token')
    @api.marshal_with(user_me)
    @Authenticate
    def get(self):
        user_id = g.user.get('owner_id')
        return user_service.get_a_user(user_id)


    @api.doc('delete account')
    @Authenticate
    def delete(self):
        user_id = g.user.get('owner_id')
        return user_service.delete_user(user_id)


# @api.route('/by_username/<username>')
# @api.param('username', 'users unique name')
# @api.response(404, 'user note found')
# class UserByUsername(Resource):

#     @api.doc('get a user by username')
#     @api.marshal_with(user_detail)
#     def get(self, username):
#         return user_service.get_user_by_username(username)
