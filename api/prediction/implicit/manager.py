from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from scipy import sparse
from sklearn.preprocessing import MinMaxScaler

from api.prediction.predictor import BasePredictor


class ImplicitPredictor(BasePredictor):
    def get_similar_items(self):
        item_vecs = self.get_model().item_factors
        item_norms = np.sqrt((item_vecs * item_vecs).sum(axis=1))

        scores = item_vecs.dot(item_vecs[self.item_id]) / item_norms
        top_idx = np.argpartition(scores, -self.k)[-self.k:]
        similar = sorted(zip(top_idx, scores[top_idx] / item_norms[self.item_id]), key=lambda x: -x[1])

        products = [product_id for product_id, score in similar]
        return BasePredictor.fetch(products)

    def get_recommended_products(self):
        sparse_user_item = joblib.load(Path.cwd() / 'api' / 'prediction' / 'implicit' / "sparse_user_item.joblib")
        user_vecs = sparse.csr_matrix(self.get_model().user_factors)
        item_vecs = sparse.csr_matrix(self.get_model().item_factors)

        user_interactions = sparse_user_item[self.user_id, :].toarray()
        user_interactions = user_interactions.reshape(-1) + 1
        user_interactions[user_interactions > 1] = 0
        rec_vector = user_vecs[self.user_id, :].dot(item_vecs.T).toarray()
        min_max = MinMaxScaler()
        rec_vector_scaled = min_max.fit_transform(rec_vector.reshape(-1, 1))[:, 0]
        recommend_vector = user_interactions * rec_vector_scaled
        content_idx = np.argsort(recommend_vector)[::-1][:self.k]

        items = []
        scores = []

        for idx in content_idx:
            items.append(idx)
            scores.append(recommend_vector[idx])

        recommendations = pd.DataFrame({'item': items, 'score': scores})

        return recommendations

    user_id = 18023

    recommendations = recommend(user_id, sparse_item_user, user_vecs, item_vecs)

    print(recommendations)
    pass


def get_model(self):
    return joblib.load(Path.cwd() / 'api' / 'prediction' / 'implicit' / "model.joblib")
