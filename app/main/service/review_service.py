from flask import g

from datetime import datetime

from .. import db

from ..model.review import Review

def create_review(data):

    new_review = Review(
        owner_id=data['owner_id'],
        title=data['title'],
        content=data['content'],
        rating=data['rating'],
        created_at=datetime.utcnow(),
        modified_at=datetime.utcnow()
    )

    save_changes(new_review)

    response_object = {
        'status' : 'success',
        'message' : 'created'
    }

    return response_object

def get_all_reviews():
    return Review.query.filter_by(owner_id=g.user.get('owner_id')).all()

def get_review_by_id(id):
    review = Review.query.filter_by(id=id, owner_id=g.user.get('owner_id')).first()

    if review:
        return review
    
    return {'status' : 'review not found'}, 404

def update_review(id, data):
    review = get_review_by_id(id)
    if review:
        for key, item in data.items():
            setattr(review, key, item)
        review.modified_at = datetime.utcnow()
        db.session.commit()
        return Review.query.get(id), 200
    else:
        return {'status' : 'item not found'}, 404

def delete_review(id):
    review = get_review_by_id(id)

    if review:
        db.session.delete(review)
        db.session.commit()
        return {'status' : 'no content'}, 204
    else:
        return {'status' : 'item not found'}, 404

def save_changes(data):
    db.session.add(data)
    db.session.commit()