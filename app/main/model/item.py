import datetime
import jwt

from .user import User
from .. import db, flask_bcrypt

class Item(db.Model):

    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(32), nullable=False)
    content = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Float, nullable=False)
    gender = db.Column(db.String(128), nullable=False)
    category = db.Column(db.String(128), nullable=False) 
    listed = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    modified_at = db.Column(db.DateTime, nullable=False)


