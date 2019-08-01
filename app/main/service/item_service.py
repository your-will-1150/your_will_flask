from flask import g

from datetime import datetime

from .. import db

from ..model.item import Item
from ..model.user import User
from ..service.user_service import get_a_user


def create_item(data):

    new_item = Item(
        owner_id=data['owner_id'],
        title=data['title'],
        content=data['content'],
        price=data['price'],
        listed=data['listed'],
        gender=data['gender'],
        category=data['category'],
        created_at=datetime.utcnow(),
        modified_at=datetime.utcnow()
    )

    save_changes(new_item)

    response_object = {
        'status' : 'success',
        'message' : 'created'
    }

    return response_object

def get_item_by_category(category):
    item = Item.query.filter_by(category=category).first()
    return item

def get_item_by_gender(gender):
    item = Item.query.filter_by(gender=gender).first()
    return item

def get_all_items():
    return Item.query.all()

def get_all_items_by_user(owner_id):
    return Item.query.filter_by(id=owner_id).all()


def get_item_by_id(id):
    item = Item.query.filter_by(id=id).first()

    if item:
        return item
    
    return {'status' : 'item not found'}, 404

def update_item(id, data):
    item2 = get_item_by_id(id)
    if item2:
        for key, item in data.items():
            setattr(item2, key, item)
        item2.modified_at = datetime.utcnow()
        db.session.commit()
        return Item.query.get(id), 200
    else:
        return {'status' : 'item not found'}, 404

def delete_item(id):
    item = get_item_by_id(id)
    if item:
        db.session.delete(item)
        db.session.commit()
        return {'status' : 'no content'}, 204
    else:
        return {'status' : 'item not found'}, 404

def delete_item_admin(id, data):
    real_dat = User.query.filter_by(id=data).first()
    item = get_item_by_id(id)
    if real_dat.admin:
        if item:
            db.session.delete(item)
            db.session.commit()
            return {'status' : 'no content'}, 204
        else:
            return {'status' : 'item not found'}, 404
    else:
        return {'status' : 'Error: Not an Admin'}

def update_item_admin(id, data):
    item2 = get_item_by_id(id)
    real_dat = User.query.filter_by(id=data['owner_id']).first()
    print(real_dat.admin, 'lolllll')
    if real_dat.admin:
        if item2:
            for key, item in data.items():
                setattr(item2, key, item)
            item2.modified_at = datetime.utcnow()
            db.session.commit()
            return Item.query.get(id), 200
        else:
            return {'status' : 'item not found'}, 404
    else:
        return {'status' : 'Error: Not an Admin'}
        


def save_changes(data):
    db.session.add(data)
    db.session.commit()

#this is generic delete 
# def delete_item(owner_id, id):
#     item = Item.query.filter_by(owner_id=owner_id).first()
#     owner = User.query.filter_by(id=id).first()
#     if item['owner_id'] == owner['user_id']:
#         db.session.delete(item)
#         db.session.commit()
#         return None, 204
#     else:
#         response = {'status' : 'failed, cannot delete other users items'}
#         return response
    # if item owner id and user id are ==
    # delete item from database
    # else, not authenticated 

# def change_listing_status(data):
#     listed = data['listed']
#     if listed_data:
#         listed = False
#     listed = True

#     return listed
# based off user inpiut, listed will change to either true or false