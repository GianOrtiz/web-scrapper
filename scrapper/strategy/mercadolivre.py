from typing import Tuple, List
from scrapper.strategy.strategy import ScrappingStrategy, Product
from bs4 import BeautifulSoup

class MercadoLivreScrappingStrategy(ScrappingStrategy):
    def scrap_product(self, content: BeautifulSoup, page: str, original_links: List[str]) -> Tuple[List[Product], List[str]]:
        list_of_products: list[Product] = []
        products = content.find_all(attrs={"class": "ui-search-result__wrapper"})
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
        link_element = raw_product.find(attrs={"class": "poly-component__title"}).find('a')
        link = link_element.get('href')
        return link

    def get_title(self, raw_product):
        title_element = raw_product.find(attrs={"class": "poly-component__title"})
        title = title_element.string
        return title

    def get_review(self, raw_product):
        review_element = raw_product.find(attrs={"class": "poly-reviews__rating"})
        if review_element is not None:
            review = review_element.string
            return review
        return None
    
    def get_price_value(self, raw_product):
        price_element = raw_product.find(attrs={"class": "andes-money-amount--cents-superscript"})
        if price_element is not None:
            price = price_element.get("aria-label")
            return price
        return None

    def retrieve_text_from_children(self, children, text):
        current_text = text
        for child in children:
            if child.string is not None:
                current_text += child.string
            try:
                if child.children is not None:
                    text = self.retrieve_text_from_children(child.children, current_text)
            except:
                # There is a situation whereas there is no children attribute and the object throws
                # an error, we pass in this situations as we do not want to do nothing with this error.
                pass
        return text

    def get_installment(self, raw_product):
        installment_element = raw_product.find(attrs={"class": "poly-price__installments"})
        if installment_element is not None:
            installment = self.retrieve_text_from_children(installment_element.children, '')
            return installment
        return None
