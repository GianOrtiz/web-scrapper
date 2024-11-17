from exporter.exporter import ProductsExporter
from exporter.json import JSONProductsExporter
from exporter.csv import CSVProductsExporter

class ExporterFactory:
  @staticmethod
  def get(type: str):
    if type == 'json':
      return JSONProductsExporter()
    elif type == 'csv':
      return CSVProductsExporter()
    
    raise Exception('Implementation of exporter not found')
