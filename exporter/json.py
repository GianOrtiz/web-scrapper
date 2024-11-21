import json

from datetime import datetime
from typing import List
from data.product import Product
from exporter.exporter import ProductsExporter

class JSONProductsExporter(ProductsExporter):
  def __init__(self, filename: str = 'products.json'):
    self.__filename = filename

  def export(self, products: List[Product]):
    with open(self.__filename, 'w+') as file:
        products_json = []
        now = datetime.now()
        for product in products:
          product_json = product.to_json()
          product_json['date'] = now.isoformat()
          products_json.append(product_json)
        json.dump(products_json, file, indent=2)