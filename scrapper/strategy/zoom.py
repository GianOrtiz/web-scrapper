from typing import Tuple, List
from scrapper.strategy.strategy import ScrappingStrategy, Product
from bs4 import BeautifulSoup

class ZoomScrappingStrategy(ScrappingStrategy):
    def scrap_product(self, content: BeautifulSoup, page: str, original_links: List[str]) -> Tuple[List[Product], List[str]]:
        list_of_products: list[Product] = []
        products = content.find_all(attrs={"data-testid": "product-card::card"})
        for raw_product in products:
            product = self.get_product(raw_product)
            list_of_products.append(product)
        return list_of_products, original_links


    def get_product(self, raw_product):
        link = self.get_link(raw_product)
        title = self.get_title(raw_product)
        review = self.get_review(raw_product)
        price_value = self.get_price_value(raw_product)
        installment = self.get_installment(raw_product)
        return Product(link, title, review, price_value, installment)

    def get_link(self, raw_product):
        raise Exception("not implemented")

    def get_title(self, raw_product):
        raise Exception("not implemented")

    def get_review(self, raw_product):
        raise Exception("not implemented")
    
    def get_price_value(self, raw_product):
        raise Exception("not implemented")
 
    def get_installment(self, raw_product):
        raise Exception("not implemented")
