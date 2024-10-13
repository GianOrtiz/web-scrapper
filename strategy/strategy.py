from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from data.product import Product

class ScrappingStrategy(ABC):
    @abstractmethod
    def scrap_product(self, content: BeautifulSoup) -> list[Product]:
        return
