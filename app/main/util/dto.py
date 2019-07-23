from flask_restplus import Namespace, fields

class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'admin': fields.Boolean(required=False, description='Set user admin privilages'),
        'public_id': fields.String(required=False, description='user public id')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password')
    })

class UserDetailDto:
    user = UserDto.api.model('user_detail', {
        'id' : fields.Integer(description='user Identifier'),
        'username' : fields.String(required=True, description='user username'),
        'registered_on' : fields.DateTime(description='time of registration'),
        'modified_at' : fields.DateTime(description='time of revision'),
    })

class UserCreateDto:
    user = UserDto.api.model('user_create', {
        'email' : fields.String(required=True,
        description='user email address'),
        'username' : fields.String(required=True, description='user username'),
        'password' : fields.String(required=True, description='user password'),
        'confirm_password' : fields.String(required=True, 
        description='users confirmation of password'),
    })

class UserUpdateDto:
    user = UserDto.api.model('user_updated', {
        'email' : fields.String(required=True, description='user email address'),
        'username' : fields.String(required=True, description='user username'),
    })

class UserMe:
    user = UserDto.api.model('user_detail', {
        'email' : fields.String(required=True, description='users email'),
        'username' : fields.String(required=True, description='user username'),
        'id' : fields.Integer(description='user Identifier'),
        'registered_on' : fields.DateTime(description='time of registration'),
        'modified_at' : fields.DateTime(description='time of revision')
    })

class ItemDto:
    api = Namespace('item', description='items')
    item = api.model('item_list_item', {
        'id' : fields.Integer(required=True, description='id of item'),
        'title' : fields.String(required=True, description='title'),
        'owner_id' : fields.String(required=True, description='id of owner'),
        'created_at' : fields.DateTime(required=True, description='when item was created')
    })

class ItemDetailDto:
    api = ItemDto.api
    item = api.model('item_detail', {
        'id' : fields.Integer(required=True, description='id of item'),
        'title' : fields.String(required=True, description='title'),
        'content' : fields.String(required=True, description='content of item'),
        'price' : fields.Float(required=True, description='price of item'),
        'owner_id' : fields.String(required=True, description='id of owner'),
        'created_at' : fields.DateTime(description='when the item was created'),
        'modified_at' : fields.DateTime(description='last revision of item')
    })

class ItemCreateDto:
    api = ItemDto.api
    item = api.model('item_create', {
        'title' : fields.String(required=True, description='title of item'),
        'content' : fields.String(required=True, description='content of item'),
        'price' : fields.Float(required=True, description='price of item')
    })

class ItemUpdateDto:
    api = ItemDto.api
    item = api.model('item_update', {
        'title' : fields.String(required=True, description='title of item'),
        'content' : fields.String(required=True, description='content of note'),
        'price' : fields.Float(required=True, description='price of item')
    })