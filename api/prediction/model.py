from api.base.model import BaseModel
from api.common import db


class SVDRecommendedProduct(BaseModel):
    __tablename__ = 'svd_recommended_products'
    products = db.Column(db.String, nullable=False)


class RBMRecommendedProduct(BaseModel):
    __tablename__ = 'rbm_recommended_products'
    products = db.Column(db.String, nullable=False)
