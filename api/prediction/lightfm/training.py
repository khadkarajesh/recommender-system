import joblib
from lightfm import LightFM
from lightfm.cross_validation import random_train_test_split
from lightfm.evaluation import precision_at_k
from lightfm.evaluation import auc_score

LIGHTFM_MODEL = "model.joblib"


def train(interactions, path):
    train_dataset, test_dataset = random_train_test_split(interactions)

    model = LightFM(learning_rate=0.05, loss='warp')
    model.fit(train_dataset, epochs=10)

    model_path = path / LIGHTFM_MODEL

    joblib.dump(model, model_path)

    train_precision = precision_at_k(model, train_dataset, k=10).mean()
    test_precision = precision_at_k(model, test_dataset, k=10).mean()

    train_auc = auc_score(model, train_dataset).mean()
    test_auc = auc_score(model, test_dataset).mean()

    return {
        'path': str(model_path),
        'auc': {
            'train': str(round(train_auc, 2)),
            'test': str(round(test_auc, 2))
        },
        'precision': {
            'train': str(round(train_precision, 2)),
            'test': str(round(test_precision, 2))
        }
    }
