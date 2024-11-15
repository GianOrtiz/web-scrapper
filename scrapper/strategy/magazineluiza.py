from typing import List
from scrapper.strategy.strategy import ScrappingStrategy, Product
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from data.product_list import UniqueProductList

class MagazineLuizaScrappingStrategy(ScrappingStrategy):
    def scrap_product(self, content: BeautifulSoup, page: str, original_links: List[str], products_list: UniqueProductList) -> List[str]:
        products = content.find_all(attrs={"data-testid": "product-card-container"})
        if len(products) > 0:
            for raw_product in products:
                product = self.get_product(raw_product, page)
                products_list.append(product)
        else:
            product = self.get_single_product(content, page)
            if product is not None:
                products_list.append(product)

        url = urlparse(page)
        original_host = url.scheme + '://' + url.netloc
        links = content.find_all('a')
        new_links = []
        for link in links:
            href = link.get('href')
            if href is not None:
                if 'magazineluiza.com.br' in href:
                    link_url = href
                else:
                    link_url = original_host + href
                if link_url not in original_links and link_url not in new_links:
                    new_links.append(link_url)
        return new_links

    def get_single_product(self, content, page):
        link = page
        title = self.get_single_title(content)
        review = self.get_single_review(content)
        price_value = self.get_single_price_value(content)
        installment = self.get_single_installment(content)
        if title is None and review is None and price_value is None and installment is None:
            return None
        return Product(link, title, review, price_value, installment)

    def get_product(self, raw_product, page):
        link = self.get_link(raw_product, page)
        title = self.get_title(raw_product)
        review = self.get_review(raw_product)
        price_value = self.get_price_value(raw_product)
        installment = self.get_installment(raw_product)
        return Product(link, title, review, price_value, installment)

    def get_link(self, raw_product, page):
        href = raw_product.get('href')
        if href is None:
            return None
        
        if 'magazineluiza.com.br' not in href:
            url = urlparse(page)
            original_host = url.scheme + '://' + url.netloc
            href = original_host + href
        return href
        

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
            installment_element = product_content.find(attrs={"data-testid": "installment"})
            if installment_element is not None:
                installment = installment_element.get_text()
                return installment
        return None

    def get_single_title(self, content):
        title_element = content.find(attrs={"data-testid": "heading-product-title"})
        if title_element is not None:
            title = title_element.string
            return title
        return None

    def get_single_review(self, content):
        review_element = content.find(attrs={"format": "score-count"})
        if review_element is not None:
            review = review_element.string
            return review
        return None
    
    def get_single_price_value(self, content):
        price_element = content.find(attrs={"data-test-id": "price-value"})
        if price_element is not None:
            price = price_element.get("aria-label")
            return price
        return None

    def get_single_installment(self, content):
        installment_element = content.find(attrs={"data-test-id": "installment"})
        if installment_element is not None:
            installment = self.retrieve_text_from_children(installment_element.children, '')
            return installment
        return None
