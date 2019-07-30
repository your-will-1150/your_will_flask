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
        'password': fields.String(default=False, required=False, description='The user password')
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
        'admin' : fields.Boolean(default=False, required=False)
    })

class UserUpdateDto:
    user = UserDto.api.model('user_updated', {
        'email' : fields.String(required=True, description='user email address'),
        'username' : fields.String(required=True, description='user username'),
        'password' : fields.String(required=True, description='user password'),
        'confirm_password' : fields.String(required=True, 
        description='users confirmation of password')
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
        'created_at' : fields.DateTime(required=True, description='when item was created'),
	'gender' : fields.String(required=True, description='gender of clothing'),
	'category' : fields.String(required=True, description='top or bottom')
    })

class ItemSpecificCat:
    api = ItemDto.api
    item = api.model('item_by_cat', {
        'title' : fields.String(required=True, description='title of item'),
        'content' : fields.String(required=True, description='content of item'),
        'price' : fields.Float(required=True, description='price of item'),
        'listed' : fields.Boolean(required=True, description='do you want this item listed?'),
	    'gender' : fields.String(required=True, descriptio='gender'),
	    'category' : fields.String(required=True, description='top or bottom')
    })

class ItemDetailDto:
    api = ItemDto.api
    item = api.model('item_detail', {
        'id' : fields.Integer(required=True, description='id of item'),
        'title' : fields.String(required=True, description='title'),
        'content' : fields.String(required=True, description='content of item'),
        'price' : fields.Float(required=True, description='price of item'),
        'listed' : fields.Boolean(required=True, description='status of listing'),
        'gender' : fields.String(required=True, description='gender'),
	'category' : fields.String(required=True, description='top or bottom'),	
	'owner_id' : fields.String(required=True, description='id of owner'),
        'created_at' : fields.DateTime(description='when the item was created'),
        'modified_at' : fields.DateTime(description='last revision of item')
    })

class ItemCreateDto:
    api = ItemDto.api
    item = api.model('item_create', {
        'title' : fields.String(required=True, description='title of item'),
        'content' : fields.String(required=True, description='content of item'),
        'price' : fields.Float(required=True, description='price of item'),
        'listed' : fields.Boolean(required=True, description='do you want this item listed?'),
	    'gender' : fields.String(required=True, descriptio='gender'),
	    'category' : fields.String(required=True, description='top or bottom')
    })

class ItemUpdateDto:
    api = ItemDto.api
    item = api.model('item_update', {
        'title' : fields.String(required=True, description='title of item'),
        'content' : fields.String(required=True, description='content of note'),
        'price' : fields.Float(required=True, description='price of item'),
        'listed' : fields.Boolean(required=True, description='status of listing'),
	'gender' : fields.String(required=True, description='gender'),
	'category' : fields.String(required=True, description='top or bottom')
    })

class ReviewDto:
    api = Namespace('review', description='reviews')
    review = api.model('review_list_item', {
        'id' : fields.Integer(required=True, description='id of review'),
        'title' : fields.String(required=True, description='title'),
        'content' : fields.String(required=True, description='content of review'),
        'rating' : fields.Integer(required=True, description='1 - 5 rating'),
        'created_at' : fields.DateTime(description='when the review was created'),   
    })

class ReviewDetailDto:
    api = ReviewDto.api
    review = api.model('review_detail', {
        'id' : fields.Integer(required=True, description='id of review'),
        'title' : fields.String(required=True, description='title'),
        'content' : fields.String(required=True, description='content of review'),
        'rating' : fields.Integer(required=True, description='1 - 5 rating'),
        'created_at' : fields.DateTime(description='when the review was created'),
        'modified_at' : fields.DateTime(description='last revision of the note')
    })

class ReviewCreateDto:
    api = ReviewDto.api
    review = api.model('review_create', {
        'title' : fields.String(required=True, description='title of review'),
        'content' : fields.String(required=True, description='content of review'),
        'rating' : fields.Integer(required=True, description='rate 1-5')
    })

class ReviewUpdateDto:
    api = ReviewDto.api
    review = api.model('review_update', {
        'title' : fields.String(required=True, description='title of review'),
        'content' : fields.String(required=True, description='give a description'),
        'rating' : fields.Integer(required=True,
        description='rate 1-5')
    })
