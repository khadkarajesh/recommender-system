from pathlib import Path

from flask import request
from flask_restful import Resource

from api.prediction.lightfm.preprocessing import preprocess
from api.prediction.lightfm.training import train
from api.prediction.manager import save_recommended_products, create_users, get_popular_products, \
    get_recommended_products, get_similar_items, search_products
from api.prediction.model import Product
from api.prediction.schema import ProductSchema


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


class SimilarProductResource(Resource):
    @classmethod
    def get(cls, product_id):
        return get_similar_items(product_id, request.args['algorithm'])


class ProductSearchResource(Resource):
    @classmethod
    def get(cls):
        query_param = request.args['name']
        return search_products(query_param)


class ModelGeneratorResource(Resource):
    @classmethod
    def post(cls):
        data_path = Path.cwd() / 'v1' / 'data'
        model_path = Path.cwd() / 'api' / 'prediction' / 'lightfm'
        interactions, weight = preprocess(data_path, model_path)
        result = train(interactions, model_path)
        return result
