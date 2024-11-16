from scrapper.strategy.strategy import ScrappingStrategy, Product
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from data.link.links import Links
from data.product_list import UniqueProductList
from data.link.aggregators.factory import LinkAggregatorFactory

class ZoomScrappingStrategy(ScrappingStrategy):
    def scrap_product(self, content: BeautifulSoup, page: str, links: Links, products_list: UniqueProductList):
        # Retrieve all products card in a list page.
        products = content.find_all(attrs={"data-testid": "product-card::card"})
        for raw_product in products:
            product = self.get_product(raw_product, page)
            products_list.append(product)

        # Retrieves news links from this page as a crawler.
        link_aggregator_factory = LinkAggregatorFactory()
        link_aggregator = link_aggregator_factory.select_strategy(page)
        link_aggregator.aggregate_links(content, page, links)

    def get_product(self, raw_product, page) -> Product:
        link = self.get_link(raw_product, page)
        title = self.get_title(raw_product)
        review = self.get_review(raw_product)
        price_value = self.get_price_value(raw_product)
        installment = self.get_installment(raw_product)
        return Product(link, title, review, price_value, installment)

    def get_link(self, raw_product, page):
        link = raw_product.get('href')

        # Some links does not include the host and use relative path, we need
        # to add the host as the prefix.
        if 'zoom.com.br' not in link:
            url = urlparse(page)
            original_host = url.scheme + '://' + url.netloc
            link = original_host + link
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
