from flask import request
from flask_restful import Resource

from api.prediction.manager import save_recommended_products, create_users, get_popular_products, \
    get_recommended_products


class RecommendedProductResource(Resource):
    @classmethod
    def get(cls, user_id):
        args = request.args
        algorithm = args.get('algorithm', 'svd')
        return get_recommended_products(user_id, algorithm)


class PopularProductResource(Resource):
    @classmethod
    def get(cls):
        return get_popular_products()


class DataSaverResource(Resource):
    @classmethod
    def post(cls):
        save_recommended_products()
        return {'status': 'ok'}


class UserSeederResource(Resource):
    @classmethod
    def post(cls):
        return create_users()
