from flask import Blueprint
from flask_restful import Api, Resource


class HelloWorldResource(Resource):
    @classmethod
    def get(cls):
        return {"say": "hi"}

    @classmethod
    def post(cls):
        pass


api_bp = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(api_bp)
api.add_resource(HelloWorldResource, '')
