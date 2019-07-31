from flask import request, g
from flask_restplus import Resource
from flask_restplus.marshalling import marshal

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



@api.route('/admin_del/<public_id>')
class Admin_Delete(Resource):
    @api.doc('delete by user id')
    @Authenticate
    def delete(self, public_id):
        data = request.json
        print(data)
        return user_service.delete_by_id(int(data['id']), public_id)

@api.route('/admin/all_users')    
class GetAllUsers(Resource):
    def get(self):
        users = user_service.get_all_users()
        if len(users) == 0:
            return {'status' : 'no items found'}, 404
        return marshal(users, user)

@api.route('/admin/<public_id>')
class AdminUpdate(Resource):
    @api.doc('update by id')
    @Authenticate
    def put(self, public_id):
        data = request.json
        return user_service.update_by_id(data, public_id)
