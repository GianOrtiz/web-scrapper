import csv

from typing import List
from data.product import Product
from exporter.exporter import ProductsExporter

class CSVProductsExporter(ProductsExporter):
  def __init__(self, filename: str = 'products.csv'):
    self.__filename = filename

  def export(self, products: List[Product]):
    products_json = []
    for product in products:
      products_json.append(product.to_json())
    keys = products_json[0].keys()
    with open(self.__filename, 'w+') as file:
      dict_writter = csv.DictWriter(file, keys)
      dict_writter.writeheader()
      dict_writter.writerows(products_json)
