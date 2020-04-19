# Pet Model
from .db import db
from .owner import Owner


class Pet(db.Document):
    name = db.StringField(required=True)
    age = db.IntField(required=False)
    raze = db.StringField(required=True)
    genre = db.ListField(db.StringField(), required=True)
    behaviour = db.ListField(db.StringField(), required=True)
    weight = db.IntField(required=False)
    black_list = db.BooleanField(require=True, default=False)
    #owner_id = db.IntField(required=True, foreign_key=True, reference=id(Owner.objects.get(id=id)))
