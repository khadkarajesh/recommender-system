from api.common import ma
from api.prediction.model import Product


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        ordered = True
        load_instance = True
