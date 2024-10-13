from bs4 import BeautifulSoup
from cache import Cache
from strategy.factory import ScrappingStrategyFactory

links = [
    "https://www.magazineluiza.com.br/lava-e-seca/eletrodomesticos/s/ed/ela1/?page=1",
    "https://www.magazineluiza.com.br/lava-e-seca/eletrodomesticos/s/ed/ela1/?page=2",
]

class Scrapper:
    def __init__(self, cache: Cache):
        self.__cache: Cache = cache
        self.__scrapping_strategy_factory: ScrappingStrategyFactory = ScrappingStrategyFactory()

    def scrap(self, page: str):
        content = self.__cache.get_page(page)
        site = BeautifulSoup(content, 'html.parser')

        strategy = self.__scrapping_strategy_factory.select_strategy(page)
        products = strategy.scrap_product(site)

location = './cache'
cache = Cache(location)
scrapper = Scrapper(cache)
scrapper.scrap(links[0])
