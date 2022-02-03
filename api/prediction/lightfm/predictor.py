from pathlib import Path

import joblib
import numpy as np

from api.prediction.predictor import BasePredictor

MODEL = "model.joblib"
ENTITY_MAPPER = "id_mapper.joblib"


def get_mapper():
    return joblib.load(Path.cwd() / 'api' / 'prediction' / 'lightfm' / ENTITY_MAPPER)


class LightFMPredictor(BasePredictor):

    def get_model(self):
        return joblib.load(Path.cwd() / 'api' / 'prediction' / 'lightfm' / MODEL)

    def get_similar_items(self):
        model = self.get_model()
        tag_embeddings = (model.item_embeddings.T
                          / np.linalg.norm(model.item_embeddings, axis=1)).T
        query_embedding = tag_embeddings[self.item_id]
        similarity = np.dot(tag_embeddings, query_embedding)
        most_similar = np.argsort(-similarity)[1:self.k]
        return most_similar

    def get_recommended_products(self):
        user_mapper = get_mapper().mapping()[0]
        item_mapper = get_mapper().mapping()[2]
        user_id = user_mapper.get(self.user_id)
        model = self.get_model()
        n_items = len(item_mapper.items())
        scores = model.predict(user_id if user_id else 0, np.arange(n_items))
        products = np.argsort(-scores).tolist()[0:self.k]
        return BasePredictor.fetch(products)
