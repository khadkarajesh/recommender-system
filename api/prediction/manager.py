import json
from pathlib import Path

import joblib
import pandas as pd
from faker import Faker
from werkzeug.security import generate_password_hash

from api.auth.user import User
from api.common import db
from api.prediction.implicit.predictor import ImplicitPredictor
from api.prediction.lightfm.predictor import LightFMPredictor
from api.prediction.model import SVDRecommendedProduct
from api.service.inventory_service import get_product_details

ALS = "als"
HYBRID = "hybrid"
SURPRISE = "surprise"


def get_popular_products(k_item=10):
    data_path = Path.cwd() / 'data' / 'user_item_interactions.csv'
    data_frame = pd.read_csv(data_path)
    popular_items = data_frame.groupby(['item']).size().reset_index()
    popular_items['count'] = popular_items[0]
    popular_items = popular_items.sort_values(by='count', ascending=False).head(k_item)
    print(popular_items['item'].values)
    return get_product_details(popular_items['item'].values)


def get_recommended_products(user_id, algorithm=SURPRISE):
    if algorithm == SURPRISE:
        svd_product = SVDRecommendedProduct.query.get(user_id)
        products = svd_product.products.split(",")
        return get_product_details([int(item) for item in products])
    elif algorithm == HYBRID:
        predictor = LightFMPredictor(user_id=user_id)
    elif algorithm == ALS:
        predictor = ImplicitPredictor(user_id=user_id)
    return predictor.get_recommended_products()


def save_recommended_products():
    with open(Path.cwd() / 'data' / 'result.json') as f:
        items = json.load(f)
        recommended_items = []
        for item in items:
            svd_recommender = SVDRecommendedProduct()
            svd_recommender.id = item
            svd_recommender.products = ','.join(str(element) for element in items[item])
            recommended_items.append(svd_recommender)
        db.session.add_all(recommended_items)
        db.session.commit()


def get_users():
    with open(Path.cwd() / 'data' / 'result.json') as f:
        items = json.load(f)
        return items.keys()


def create_users():
    print("data seeding process started ......")
    data_path = Path.cwd() / 'data' / 'users.csv'
    data_frame = pd.read_csv(data_path)
    users = []
    test_users = get_users()
    for t_user in test_users:
        row = data_frame[data_frame['id'] == t_user]
        if row['gender'].any() and row['date_of_birth'].any():
            faker = Faker()
            user = User()
            user.id = t_user
            user.first_name = faker.unique.first_name()
            user.last_name = faker.unique.last_name()
            user.gender = row['gender'].values[0]
            user.date_of_birth = row['date_of_birth'].values[0]
            user.password = generate_password_hash('password')
            print(user)
            users.append(user)
    db.session.add_all(users)
    db.session.commit()
    return {'message': 'ok'}


def get_similar_items(item_id, algorithm):
    if algorithm == SURPRISE:
        knn = joblib.load(Path.cwd() / 'api' / 'prediction' / 'knn.joblib')
        products = knn.get_neighbors(int(item_id), k=10)
        return get_product_details(products)
    elif algorithm == HYBRID:
        predictor = LightFMPredictor(item_id=int(item_id))
    elif algorithm == ALS:
        predictor = ImplicitPredictor(item_id=int(item_id))
    products = predictor.get_similar_items()
    return get_product_details(products)
