import time

from bs4 import BeautifulSoup
from cache import Cache
from strategy.factory import ScrappingStrategyFactory
from data.product import Product
from urllib.parse import urlparse

links = [
    "https://www.magazineluiza.com.br/lava-e-seca/eletrodomesticos/s/ed/ela1/?page=1",
    "https://www.zoom.com.br/lavadora-roupas/lava-e-seca",
    "https://lista.mercadolivre.com.br/eletrodomesticos/lavadores/maquinas-lavar/maquina-lava-e-seca_NoIndex_True"
]

class Scrapper:
    def __init__(self, cache: Cache, links: list[str]):
        self.__links = links
        self.__cache: Cache = cache
        self.__scrapping_strategy_factory: ScrappingStrategyFactory = ScrappingStrategyFactory()

    def scrap_all_sites(self) -> list[Product]:
        products: list[Product] = []
        for link in self.__links:
            print('Retrieve content data for ', link)
            new_products = self.scrap(link)
            products.extend(new_products)
            print('Waiting to retrieve new URL')
            time.sleep(30)
        return products

    def scrap(self, page: str) -> list[Product]:
        content = self.__cache.get_page(page)
        site = BeautifulSoup(content, 'html.parser')
        
        url = urlparse(page)
        original_host = url.scheme + '://' + url.netloc
        links = site.find_all('a')
        for link in links:
            href = link.get('href')
            if href is not None:
                if href.find('page=') > 0:
                    link_url = original_host + href
                    if link_url not in self.__links:
                        self.__links.append(link_url)

        strategy = self.__scrapping_strategy_factory.select_strategy(page)
        products = strategy.scrap_product(site)
        return products

location = './cache'
cache = Cache(location)
scrapper = Scrapper(cache, links)
products = scrapper.scrap_all_sites()
