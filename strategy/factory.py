from strategy.strategy import ScrappingStrategy
from strategy.magazineluiza import MagazineLuizaScrappingStrategy

class ScrappingStrategyFactory:
    def select_strategy(self, page: str) -> ScrappingStrategy:
        if page.find('magazineluiza'):
            return MagazineLuizaScrappingStrategy()
        return ScrappingStrategy()
