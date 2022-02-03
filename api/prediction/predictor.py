from abc import ABC, abstractmethod

from api.service.inventory_service import get_product_details


class BasePredictor(ABC):
    def __init__(self, **kwargs):
        self.item_id = kwargs.get('item_id', '')
        self.user_id = kwargs.get('user_id', '')
        self.k = kwargs.get('k', 10)

    @abstractmethod
    def get_similar_items(self):
        pass

    @abstractmethod
    def get_recommended_products(self):
        pass

    @abstractmethod
    def get_model(self):
        pass

    @classmethod
    def fetch(cls, items):
        return get_product_details(items)
