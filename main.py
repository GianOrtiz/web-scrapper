import json

from scrapper.scrapper import Scrapper
from data.cache import Cache

links = [
    "https://www.magazineluiza.com.br/lava-e-seca/eletrodomesticos/s/ed/ela1/?page=1",
    "https://www.zoom.com.br/lavadora-roupas/lava-e-seca",
    "https://lista.mercadolivre.com.br/eletrodomesticos/lavadores/maquinas-lavar/maquina-lava-e-seca_NoIndex_True"
]    
location = './cache'

if __name__ == '__main__':
    cache = Cache(location)
    scrapper = Scrapper(cache, links)
    products = scrapper.scrap_all_sites()

    # Write products retrieved to a JSON file.
    with open('products.json', 'w+') as file:
        products_json = []
        for product in products:
            products_json.append(product.to_json())
        json.dump(products_json, file, indent=2)
