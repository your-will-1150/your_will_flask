import datetime
import jwt

from .user import User
from .. import db, bcrypt

class Item(db.Model):

    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner_id = db.Column(db.Integer, db.ForeingKey('users.id'), nullable=False)
    item_title = db.Column(db.String(32), nullable=False)
    item_description = db.Column(db.String(128), nullable=False)
    item_price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    modified_at = db.Column(db.DateTime, nullable=False)


