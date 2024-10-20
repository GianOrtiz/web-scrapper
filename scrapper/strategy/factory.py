from scrapper.strategy.strategy import ScrappingStrategy
from scrapper.strategy.magazineluiza import MagazineLuizaScrappingStrategy
from scrapper.strategy.zoom import ZoomScrappingStrategy
from scrapper.strategy.mercadolivre import MercadoLivreScrappingStrategy

class ScrappingStrategyFactory:
    def select_strategy(self, page: str) -> ScrappingStrategy:
        if page.find('magazineluiza') >= 0:
            return MagazineLuizaScrappingStrategy()
        elif page.find('zoom') >= 0:
            return ZoomScrappingStrategy()
        elif page.find('mercadolivre') >= 0:
            return MercadoLivreScrappingStrategy()
        return ScrappingStrategy()
