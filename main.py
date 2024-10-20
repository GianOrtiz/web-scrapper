from scrapper.scrapper import Scrapper
from data.cache import Cache

links = [
    "https://www.magazineluiza.com.br/lava-e-seca/eletrodomesticos/s/ed/ela1/?page=1",
    # "https://www.zoom.com.br/lavadora-roupas/lava-e-seca", NOT IMPLEMENTED YET
    # "https://lista.mercadolivre.com.br/eletrodomesticos/lavadores/maquinas-lavar/maquina-lava-e-seca_NoIndex_True" NOT IMPLEMENTED YET
]    
location = './cache'

if __name__ == '__main__':
    cache = Cache(location)
    scrapper = Scrapper(cache, links)
    products = scrapper.scrap_all_sites()
