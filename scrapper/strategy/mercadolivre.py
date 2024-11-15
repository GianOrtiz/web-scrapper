import re

from typing import List
from scrapper.strategy.strategy import ScrappingStrategy, Product
from bs4 import BeautifulSoup
from data.product_list import UniqueProductList

class MercadoLivreScrappingStrategy(ScrappingStrategy):
    def scrap_product(self, content: BeautifulSoup, page: str, original_links: List[str], products_list: UniqueProductList) -> List[str]:
        products = content.find_all(attrs={"class": "ui-search-result__wrapper"})
        if len(products) > 0:
            for raw_product in products:
                product = self.get_product(raw_product)
                products_list.append(product)
        else:
            product = self.get_single_product(content, page)
            products_list.append(product)

        pattern = re.compile("https://lista\.mercadolivre\.com\.br/.*_[0-9]*_NoIndex_True|https://click1\.mercadolivre\.com\.br/.*|https://produto\.mercadolivre\.com\.br/.*")
        links = content.find_all('a')
        new_links = []
        for link in links:
            href = link.get('href')
            if href is not None:
                if pattern.match(href) is not None and '/noindex/' not in href:
                    link_url = href
                    if link_url not in original_links and link_url not in new_links:
                        new_links.append(link_url)
        return new_links

    def get_single_product(self, content, page):
        link = page
        title = self.get_single_title(content)
        review = self.get_single_review(content)
        price_value = self.get_single_price_value(content)
        installment = self.get_single_installment(content)
        return Product(link, title, review, price_value, installment)

    def get_product(self, raw_product):
        link = self.get_link(raw_product)
        title = self.get_title(raw_product)
        review = self.get_review(raw_product)
        price_value = self.get_price_value(raw_product)
        installment = self.get_installment(raw_product)
        return Product(link, title, review, price_value, installment)

    def get_link(self, raw_product):
        title_element = raw_product.find(attrs={"class": "poly-component__title"})
        if title_element is not None:
            link_element = title_element.find('a')
            link = link_element.get('href')
            return link
        return None

    def get_title(self, raw_product):
        title_element = raw_product.find(attrs={"class": "poly-component__title"})
        if title_element is not None:
            title = title_element.string
            return title
        return None

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

    def get_single_title(self, content):
        title_element = content.find(attrs={"class": "ui-pdp-title"})
        if title_element is not None:
            title = title_element.string
            return title
        return None

    def get_single_review(self, content):
        review_element = content.find(attrs={"class": "ui-pdp-review__rating"})
        if review_element is not None:
            review = review_element.string
            return review
        return None
    
    def get_single_price_value(self, content):
        price_element = content.find(attrs={"class": "andes-money-amount--cents-superscript"})
        if price_element is not None:
            price = price_element.get("aria-label")
            return price
        return None

    def get_single_installment(self, content):
        installment_element = content.find(attrs={"id": "pricing_price_subtitle"})
        if installment_element is not None:
            installment = self.retrieve_text_from_children(installment_element.children, '')
            return installment
        return None
