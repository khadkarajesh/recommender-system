from flask_restful import Resource

from api.data.manager import insert_data


class DataSeederResource(Resource):
    @classmethod
    def post(cls):
        insert_data()
        pass
