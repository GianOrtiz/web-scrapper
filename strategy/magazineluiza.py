from strategy.strategy import ScrappingStrategy, Product
from bs4 import BeautifulSoup

class MagazineLuizaScrappingStrategy(ScrappingStrategy):
    def find_product_in_magazine_luiza(self, tag):
        return tag.has_attr("data-testid") and tag["data-testid"] == "product-card-container" 

    def scrap_product(self, content: BeautifulSoup) -> list[Product]:
        list_of_products: list[Product] = []
        products = content.find_all(attrs={"data-testid": "product-card-container"})
        for product in products:
            link = product.get('href')
            product_content = product.find(attrs={"data-testid": "product-card-content"})
            product_title = product_content.find(attrs={"data-testid": "product-title"}).string
            product_review_div = product_content.find(attrs={"data-testid": "review"})
            product_review = product_review_div.find('span').string
            # price_original = product_content.find(attrs={"data-testid": "price-original"}).string
            price_value = product_content.find(attrs={"data-testid": "price-value"}).get_text()
            installment = product_content.find(attrs={"data-testid": "installment"}).get_text()
            list_of_products.append(Product(link, product_title, product_review, price_value, installment))
        return list_of_products
