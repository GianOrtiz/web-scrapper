from strategy.strategy import ScrappingStrategy
from strategy.magazineluiza import MagazineLuizaScrappingStrategy
from strategy.pontofrio import PontoFrioScrappingStrategy
from strategy.carrefour import CarrefourScrappingStrategy
from strategy.zoom import ZoomScrappingStrategy
from strategy.mercadolivre import MercadoLivreScrappingStrategy

class ScrappingStrategyFactory:
    def select_strategy(self, page: str) -> ScrappingStrategy:
        if page.find('magazineluiza') >= 0:
            return MagazineLuizaScrappingStrategy()
        elif page.find('zoom') >= 0:
            return ZoomScrappingStrategy()
        elif page.find('mercadolivre') >= 0:
            return MercadoLivreScrappingStrategy()
        return ScrappingStrategy()
