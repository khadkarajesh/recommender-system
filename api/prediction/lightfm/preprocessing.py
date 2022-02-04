import joblib
import pandas as pd
from lightfm.data import Dataset

MAPPER_NAME = "id_mapper.joblib"


def preprocess(data_path, matrix_path):
    users_df = pd.read_csv(f"{data_path}/users.csv")
    items_df = pd.read_csv(f"{data_path}/items.csv")
    user_item_interaction_df = pd.read_csv(f"{data_path}/user_item_interactions.csv")

    items_df['brand'] = items_df['brand'].astype('category')
    items_df['brand'] = items_df['brand'].cat.codes
    items_df['category'] = items_df['category'].astype('category')
    items_df['category'] = items_df['category'].cat.codes
    items_features = [(row['price'], row['brand'], row['category']) for index, row in items_df.iterrows()]

    users_df['gender'] = users_df['gender'].astype('category')
    users_df['gender'] = users_df['gender'].cat.codes
    user_features = [(row['age'], row['gender']) for index, row in users_df.iterrows()]

    dataset = Dataset()
    dataset.fit(users_df['id'].values, items_df['id'].values, user_features=user_features, item_features=items_features)

    dataset_matrix = matrix_path / MAPPER_NAME
    joblib.dump(dataset, dataset_matrix)

    interactions, weights = dataset.build_interactions(
        (row['user'], row['item'], row['rating']) for index, row in user_item_interaction_df.iterrows())
    return interactions, weights
