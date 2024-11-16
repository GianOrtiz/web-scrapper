from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from data.product import Product
from data.product_list import UniqueProductList
from data.link.links import Links

class ScrappingStrategy(ABC):
    @abstractmethod
    def scrap_product(self, content: BeautifulSoup, page: str, links: Links, products_list: UniqueProductList):
        return
