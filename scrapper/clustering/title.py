from typing import List
from rapidfuzz import process, fuzz
from data.product import Product

SIMILARITY_THRESHOLD = 90

def cluster_products_by_titles(products: List[Product]):
  titles = [product.title for product in products]
  clusters = []
  checked_titles = set()

  for product in products:
    if product.title in checked_titles:
        continue
    matches = process.extract(product.title, titles, scorer=fuzz.ratio, score_cutoff=SIMILARITY_THRESHOLD)
    cluster = [match[0] for match in matches]
    checked_titles.update(cluster)
    clusters.append(cluster)

  for product in products:
    for cluster in clusters:
      if product.title in cluster:
        product.cluster = cluster[0]
