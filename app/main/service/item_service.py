from flask import g

from datetime import datetime

from .. import db

from ..model.item import Item


def create_item(data):

    new_item = Item(
        owner_id=data['owner_id'],
        title=data['title'],
        content=data['content'],
        price=data['price'],
        created_at=datetime.utcnow(),
        modified_at=datetime.utcnow()
    )

    save_changes(new_item)

    response_object = {
        'status' : 'success',
        'message' : 'created'
    }

    return response_object


def get_all_items():
    return Item.query.filter_by(owner_id=g.user.get('owner_id')).all()

def get_item_by_id(id):
    item = Item.query.filter_by(id=id, owner_id=g.user.get('owner_id')).first()

    if item:
        return item
    
    return {'status' : 'item not found'}, 404

def update_item(id, data):
    item2 = get_item_by_id(id)
    if item:
        for key, item in data.items():
            setattr(item2, key, item)
        note.modified_at = datetime.utcnow()
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

def save_changes(data):
    db.session.add(data)
    db.session.commit()