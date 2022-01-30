from flask import request
from flask_restful import Resource

from api.auth.manager import login
from api.auth.schema import UserSchema


class LoginResource(Resource):
    @classmethod
    def post(cls):
        user_schema = UserSchema()
        user = user_schema.load(request.json)
        return login(user.username, user.password)
