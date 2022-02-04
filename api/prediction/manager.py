import json
import os
from pathlib import Path

import boto3
import botocore
import joblib
import numpy as np
import pandas as pd
from faker import Faker
from werkzeug.security import generate_password_hash

from api.auth.user import User
from api.common import db
from api.prediction.implicit.predictor import ImplicitPredictor
from api.prediction.lightfm.predictor import LightFMPredictor
from api.prediction.model import SVDRecommendedProduct, Product
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
    x = popular_items['item'].values
    np.random.shuffle(x)
    return get_product_details(x)


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


def search_products(search_term):
    products = Product.query.filter(Product.title.contains(search_term))
    products_ids = [product.id for product in products]
    return get_product_details(products_ids)


MODEL_PATH = Path.cwd() / 'api' / 'prediction' / 'lightfm'
ID_MAPPER = MODEL_PATH / 'id_mapper.joblib'
MODEL = MODEL_PATH / 'model.joblib'

MAPPER_KEY = 'id_mapper.joblib'
MODEL_KEY = "model.joblib"

USER_ITEM_INTERACTIONS_KEY = "user_item_interactions.csv"
USER_INTERACTION_PATH = Path.cwd() / 'data'
USER_INTERACTION = USER_INTERACTION_PATH / USER_ITEM_INTERACTIONS_KEY


def download():
    s3 = boto3.resource('s3', aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'))

    try:
        s3.Bucket(os.environ.get('BUCKET_NAME')).download_file(MAPPER_KEY, str(ID_MAPPER))
        s3.Bucket(os.environ.get('BUCKET_NAME')).download_file(MODEL_KEY, str(MODEL))
        s3.Bucket(os.environ.get('BUCKET_NAME')).download_file(USER_ITEM_INTERACTIONS_KEY, str(USER_INTERACTION))
        return {"success": "true"}
    except botocore.exceptions.ClientError as e:
        print(f"Exception while downloading models{e}")
        return e.response['Error']['Code']
