import time

from typing import List
from bs4 import BeautifulSoup
from scrapper.strategy.factory import ScrappingStrategyFactory
from data.product import Product
from data.cache import Cache
from data.product_list import UniqueProductList
from data.link.links import Links
from scrapper.clustering.title import cluster_products_by_titles

class Scrapper:
    def __init__(self, cache: Cache, links: Links):
        self.__links = links
        self.__cache: Cache = cache
        self.__scrapping_strategy_factory: ScrappingStrategyFactory = ScrappingStrategyFactory()
        self.__products_list = UniqueProductList()

    def scrap_all_sites(self) -> List[Product]:
        while True:
            link = self.__links.pop()
            retrieved_from_cache = self.scrap(link)
            if retrieved_from_cache == False:
                # Waits before fetching another page.
                time.sleep(20)
            print('Retrieved content data for ', link, self.__products_list.length())
            # Stops in a threshold number of products.
            if self.__products_list.length() > 2000:
                break
        cluster_products_by_titles(self.__products_list.products)
        return self.__products_list.products

    def scrap(self, page: str) -> bool:
        content, retrieved_from_cache = self.__cache.get_page(page)
        site = BeautifulSoup(content, 'html.parser')
        strategy = self.__scrapping_strategy_factory.select_strategy(page)
        strategy.scrap_product(site, page, self.__links, self.__products_list)
        return retrieved_from_cache
