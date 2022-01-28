import uuid
from datetime import datetime

from api.common import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.INT, primary_key=True)
    created_at = db.Column(db.DateTime)

    def __init__(self, **kwargs):
        super(BaseModel, self).__init__(**kwargs)
        self.created_at = datetime.utcnow()
