import json

from typing import List
from data.product import Product
from exporter.exporter import ProductsExporter

class JSONProductsExporter(ProductsExporter):
  def __init__(self, filename: str = 'products.json'):
    self.__filename = filename

  def export(self, products: List[Product]):
    with open(self.__filename, 'w+') as file:
        products_json = []
        for product in products:
          products_json.append(product.to_json())
        json.dump(products_json, file, indent=2)