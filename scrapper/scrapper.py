import time

from typing import List, Tuple
from bs4 import BeautifulSoup
from scrapper.strategy.factory import ScrappingStrategyFactory
from data.product import Product
from data.cache import Cache

class Scrapper:
    def __init__(self, cache: Cache, links: List[str]):
        self.__links = links
        self.__cache: Cache = cache
        self.__scrapping_strategy_factory: ScrappingStrategyFactory = ScrappingStrategyFactory()

    def scrap_all_sites(self) -> List[Product]:
        products: List[Product] = []
        for link in self.__links:
            print('Retrieve content data for ', link)
            new_products, retrieved_from_cache = self.scrap(link)
            products.extend(new_products)
            if retrieved_from_cache == False:
                # Waits before fetching another page.
                time.sleep(30)
            # Stops in a threshold number of products.
            if len(products) > 1500:
                break
        return products

    def scrap(self, page: str) -> Tuple[List[Product], bool]:
        content, retrieved_from_cache = self.__cache.get_page(page)
        site = BeautifulSoup(content, 'html.parser')
        strategy = self.__scrapping_strategy_factory.select_strategy(page)
        products, links = strategy.scrap_product(site, page, self.__links)
        self.__links.extend(links)
        return products, retrieved_from_cache
