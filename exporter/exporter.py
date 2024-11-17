from abc import ABC, abstractmethod
from typing import List
from data.product import Product

class ProductsExporter(ABC):
    @abstractmethod
    def export(self, products: List[Product]):
        return
