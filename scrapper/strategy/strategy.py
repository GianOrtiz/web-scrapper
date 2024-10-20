from typing import Tuple, List
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from data.product import Product

class ScrappingStrategy(ABC):
    @abstractmethod
    def scrap_product(self, content: BeautifulSoup, page: str, links: List[str]) -> Tuple[List[Product], List[str]]:
        return
