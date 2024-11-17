from typing import List
from rapidfuzz import process, fuzz
from data.product import Product

SIMILARITY_THRESHOLD = 90

def cluster_products_by_titles(products: List[Product]):
  titles = [product.title for product in products]
  clusters = []

  for product in products:
    matches = process.extract(product.title, titles, scorer=fuzz.ratio, score_cutoff=SIMILARITY_THRESHOLD)
    cluster = [match[0] for match in matches]
    clusters.append(cluster)

  for product in products:
    for cluster in clusters:
      if product.title in cluster:
        product.cluster = clusters.index(cluster)
