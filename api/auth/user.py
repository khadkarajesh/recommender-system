import json

from api.base.model import BaseModel
from api.common import db


class User(BaseModel):
    __tablename__ = 'users'
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String, nullable=False)
    username = db.Column(db.BIGINT, nullable=False)

    def __str__(self):
        return f'name :{self.first_name}, last_name: {self.last_name}, gender:{self.gender}, date_of_birth:{self.date_of_birth}'

    def to_json(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'date_of_birth': json.dumps(self.date_of_birth),
            'gender': self.gender
        }
