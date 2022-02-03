from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from scipy import sparse
from sklearn.preprocessing import MinMaxScaler

from api.prediction.lightfm.predictor import ENTITY_MAPPER
from api.prediction.predictor import BasePredictor


def get_mapper():
    return joblib.load(Path.cwd() / 'api' / 'prediction' / 'lightfm' / ENTITY_MAPPER)


class ImplicitPredictor(BasePredictor):
    def get_model(self):
        return joblib.load(Path.cwd() / 'api' / 'prediction' / 'implicit' / "model.joblib")

    def get_similar_items(self):
        ids, scores = self.get_model().similar_items(int(self.item_id))
        return BasePredictor.fetch(ids)

    def get_recommended_products(self):
        interactions = joblib.load(Path.cwd() / 'api' / 'prediction' / 'implicit' / "interactions.joblib")
        id_mapper = get_mapper()
        ids, scores = self.get_model().recommend(id_mapper[self.user_id],
                                                 interactions.tocsr()[id_mapper[self.user_id]],
                                                 N=self.k)
        return BasePredictor.fetch(ids)
