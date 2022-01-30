from pathlib import Path

import joblib
import pandas as pd


def get_similar_items(product_id):
    model = joblib.load(Path.cwd() / 'api/prediction' / 'knn.joblib')
    return model.get_neighbors(product_id, k=10)


def get_popular_items(top_k=10):
    interaction = pd.read_csv(Path.cwd() / 'data' / 'user_item_interactions.csv')
    popular_items = interaction.groupby('item_id')['rating'].mean().sort_values(ascending=False).head(
        top_k).reset_index()
    return popular_items['item_id'].values
