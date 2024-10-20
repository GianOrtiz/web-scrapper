from typing import Tuple, List
from scrapper.strategy.strategy import ScrappingStrategy, Product
from bs4 import BeautifulSoup
from urllib.parse import urlparse

class ZoomScrappingStrategy(ScrappingStrategy):
    def scrap_product(self, content: BeautifulSoup, page: str, original_links: List[str]) -> Tuple[List[Product], List[str]]:
        list_of_products: list[Product] = []
        products = content.find_all(attrs={"data-testid": "product-card::card"})
        for raw_product in products:
            product = self.get_product(raw_product)
            list_of_products.append(product)

        url = urlparse(page)
        original_host = url.scheme + '://' + url.netloc
        links = content.find_all('a')
        for link in links:
            href = link.get('href')
            if href is not None:
                if href.find('page=') > 0:
                    link_url = original_host + href
                    if link_url not in original_links:
                        original_links.append(link_url)
        
        return list_of_products, original_links


    def get_product(self, raw_product) -> Product:
        link = self.get_link(raw_product)
        title = self.get_title(raw_product)
        review = self.get_review(raw_product)
        price_value = self.get_price_value(raw_product)
        installment = self.get_installment(raw_product)
        return Product(link, title, review, price_value, installment)

    def get_link(self, raw_product):
        link = raw_product.get('href')
        return link

    def get_title(self, raw_product):
        title_component = raw_product.find(attrs={"data-testid": "product-card::name"})
        if title_component is not None:
            title = title_component.text
            return title
        return None

    def get_review(self, raw_product):
        review_component = raw_product.find(attrs={"data-testid": "product-card::rating"})
        if review_component is not None:
            review = review_component.text
            return review
        return None

    def get_price_value(self, raw_product):
        price_component = raw_product.find(attrs={"data-testid": "product-card::price"})
        if price_component is not None:
            price = price_component.text
            return price
        return None
 
    def get_installment(self, raw_product):
        installment_component = raw_product.find(attrs={"data-testid": "product-card::installment"})
        if installment_component is not None:
            installment = installment_component.text
            return installment
        return None
