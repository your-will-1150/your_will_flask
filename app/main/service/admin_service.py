import uuid 
import datetime import datetime 
from .. import db
from ..model.user import User
from ..model.item import Item
from ..model.review import Review
from service import user_service
import re 

check_for_ad = user_service.get_user_by_username
get_user_by_id = user_service.get_a_user

# first user is admin, can change other users to admin
# instead of this function below, build off of generic create user
def confirm_admin(data):
    user = User.query.filter_by(email=data['email']).first()
    if check_for_ad(user.username) != True:
        response_object = {
            'status' : 'fail',
            'message' : 'Not an Admin'
        }
        return False, response_object
    
    else:
        return True

def get_all_users():
    if confirm_admin:
        return User.query.all()
    
    else:
        response_object = {
            'status' : 'fail',
            'message' : 'Not an Admin'
        }
        return response_object

def delete_user_admin(username):
    if confirm_admin:
        user_delete = get_user_by_id(username)
        db.session.delete(user_delete)
        db.session.commit()
        return None, 204

    else: 
        response_object = {
            'status' : 'fail',
            'message' : 'Not an Admin'
        }
        return response_object 

def update_user_admin(username, data):
    if confirm_admin:
        user = get_a_user(username)
        for key, item in data.items():
            setattr(user, key, item)
        user.modified_at = datetime.utcnow()
        db.session.commit()
        response = {'status' : 'updated user'}
        return response, 200
    
    else: 
        response_object = {
            'status' : 'fail',
            'message' : 'Not an Admin'
        }
        return response_object 

def update_item_admin(owner_id, data):

    # get item by username, then update the item 
    if confirm_admin:
        item2 = get_item_by_id(owner_id)
        if item2:
            for key, item in data.items():
                setattr(item2, key, item)
            item2.modified_at = datetime.utcnow()
            db.session.commit()
            return Item.query.get(id), 200
        else:
            return {'status' : 'item not found'}, 404
    else:
        response_object = {
            'status' : 'fail',
            'message' : 'Not an Admin'
        }
        return response_object 
    
def delete_item_admin(username):
    



        
