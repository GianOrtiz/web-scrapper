from typing import Tuple, List
from scrapper.strategy.strategy import ScrappingStrategy, Product
from bs4 import BeautifulSoup
from urllib.parse import urlparse

class MagazineLuizaScrappingStrategy(ScrappingStrategy):
    def scrap_product(self, content: BeautifulSoup, page: str, original_links: List[str]) -> Tuple[List[Product], List[str]]:
        list_of_products: list[Product] = []
        products = content.find_all(attrs={"data-testid": "product-card-container"})
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

        return list_of_products, links


    def get_product(self, raw_product):
        link = self.get_link(raw_product)
        title = self.get_title(raw_product)
        review = self.get_review(raw_product)
        price_value = self.get_price_value(raw_product)
        installment = self.get_installment(raw_product)
        return Product(link, title, review, price_value, installment)

    def get_link(self, raw_product):
        return raw_product.get('href')

    def get_title(self, raw_product):
        product_content = raw_product.find(attrs={"data-testid": "product-card-content"})
        if product_content is not None:
            product_title = product_content.find(attrs={"data-testid": "product-title"}).string
            return product_title
        return None

    def get_review(self, raw_product):
        product_content = raw_product.find(attrs={"data-testid": "product-card-content"})
        product_review_div = product_content.find(attrs={"data-testid": "review"})
        if product_review_div is not None:
            product_review = product_review_div.find('span').string
            return product_review
        return None
    
    def get_price_value(self, raw_product):
        product_content = raw_product.find(attrs={"data-testid": "product-card-content"})
        if product_content is not None:
            price_value = product_content.find(attrs={"data-testid": "price-value"}).get_text()
            return price_value
        return None
 
    def get_installment(self, raw_product):
        product_content = raw_product.find(attrs={"data-testid": "product-card-content"})
        if product_content is not None:
            installment = product_content.find(attrs={"data-testid": "installment"}).get_text()
            return installment
        return None
