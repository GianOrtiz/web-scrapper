import time

from typing import List
from bs4 import BeautifulSoup
from scrapper.strategy.factory import ScrappingStrategyFactory
from data.product import Product
from data.cache import Cache
from data.product_list import UniqueProductList

class Scrapper:
    def __init__(self, cache: Cache, links: List[str]):
        self.__links = links
        self.__cache: Cache = cache
        self.__scrapping_strategy_factory: ScrappingStrategyFactory = ScrappingStrategyFactory()
        self.__products_list = UniqueProductList()

    def scrap_all_sites(self) -> List[Product]:
        for link in self.__links:
            retrieved_from_cache = self.scrap(link)
            if retrieved_from_cache == False:
                # Waits before fetching another page.
                time.sleep(20)
            print('Retrieved content data for ', link, self.__products_list.length())
            # Stops in a threshold number of products.
            if self.__products_list.length() > 4500:
                break
        return self.__products_list.products

    def scrap(self, page: str) -> bool:
        content, retrieved_from_cache = self.__cache.get_page(page)
        site = BeautifulSoup(content, 'html.parser')
        strategy = self.__scrapping_strategy_factory.select_strategy(page)
        new_links = strategy.scrap_product(site, page, self.__links, self.__products_list)
        self.__links.extend(new_links)
        return retrieved_from_cache
