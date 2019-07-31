import datetime
import jwt

from .user import User
from ..import db, flask_bcrypt

class Review(db.Model):

    __tablename__ = 'review'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    username = db.Column(db.String(128), db.ForeignKey('users.username'), nullable=False)
    title = db.Column(db.String(32), nullable=False)
    content = db.Column(db.String(128), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    modified_at = db.Column(db.DateTime, nullable=False)
