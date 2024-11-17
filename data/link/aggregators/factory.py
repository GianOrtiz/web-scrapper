from data.link.aggregators.magazineluiza import MagazineLuizaLinkAggregator
from data.link.aggregators.mercadolivre import MercadoLivreLinkAggregator
from data.link.aggregators.zoom import ZoomLinkAggregator
from data.link.link_aggregator import LinkAggregator

class LinkAggregatorFactory:
    def select_strategy(self, page: str) -> LinkAggregator:
        if page.find('magazineluiza') >= 0:
            return MagazineLuizaLinkAggregator()
        elif page.find('zoom') >= 0:
            return ZoomLinkAggregator()
        elif page.find('mercadolivre') >= 0:
            return MercadoLivreLinkAggregator()
        return ScrappingStrategy()
