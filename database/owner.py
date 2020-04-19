# Pet Owner Model
from .db import db


class Owner(db.Document):
    name = db.StringField(required=True)
    phone = db.StringField(required=False)
    ci_owner = db.StringField(required=True, unique=True)
    genre = db.ListField(db.StringField(), required=True)
    black_list = db.BooleanField(require=True, default=False)