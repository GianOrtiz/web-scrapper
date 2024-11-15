from typing import List
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from data.product import Product
from data.product_list import UniqueProductList

class ScrappingStrategy(ABC):
    @abstractmethod
    def scrap_product(self, content: BeautifulSoup, page: str, links: List[str], products_list: UniqueProductList) -> List[str]:
        return
