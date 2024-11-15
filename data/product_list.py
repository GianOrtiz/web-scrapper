from typing import List
from data.product import Product

class UniqueProductList:
    def __init__(self):
        self.__products: List[Product] = []
        self.__products_links: List[str] = []

    def append(self, product: Product):
        # Appends to the product list only if there is no product with the same link.
        if product.link not in self.__products_links:
            self.__products_links.append(product.link)
            self.__products.append(product)
    
    def length(self) -> int:
        return len(self.__products)

    @property
    def products(self) -> List[Product]:
        return self.__products
