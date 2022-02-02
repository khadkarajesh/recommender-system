from api.base.model import BaseModel
from api.common import db


class SVDRecommendedProduct(BaseModel):
    __tablename__ = 'svd_recommended_products'
    products = db.Column(db.String, nullable=False)


class RBMRecommendedProduct(BaseModel):
    __tablename__ = 'rbm_recommended_products'
    products = db.Column(db.String, nullable=False)


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.INT, nullable=False, primary_key=True)
    title = db.Column(db.String, nullable=False)
    brand = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
