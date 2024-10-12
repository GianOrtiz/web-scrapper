import requests
import json
from bs4 import BeautifulSoup

cache_file = 'cache.html'

links = [
    "https://www.magazineluiza.com.br/lava-e-seca/eletrodomesticos/s/ed/ela1/"
]

def find_product_in_magazine_luiza(tag):
    return tag.has_attr("data-testid") and tag["data-testid"] == "product-card-container" 

def get_content(cache=False):
    if cache:
        with open(cache_file, 'r') as f:
            content = f.read()
            return content
    else:
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
            "Accept-Encoding": "gzip, deflate, br", 
	        "Accept-Language": "en-US,en;q=0.9", 
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",

        }
        page_request = requests.get(links[0], headers=headers)
        content = page_request.content
        print(content)
        # Writes the received content to a cache to avoid unecessary requests.
        with open(cache_file, 'w+') as f:
            f.write(content.decode('utf-8'))
        return content
        
content = get_content(False)
site = BeautifulSoup(content, 'html.parser')
 
products = site.find_all(attrs={"data-testid": "product-card-container"})
print(products[1].find(attrs={"data-testid": "product-card-content"}))
for product in products:
    link = product.get('href')
    product_content = product.find(attrs={"data-testid": "product-card-content"})
    product_title = product_content.find(attrs={"data-testid": "product-title"}).string
    product_review_div = product_content.find(attrs={"data-testid": "review"})
    product_review = product_review_div.find('span').string
    price_original = product_content.find(attrs={"data-testid": "price-original"}).string
    price_value = product_content.find(attrs={"data-testid": "price-value"}).get_text()
    installment = product_content.find(attrs={"data-testid": "installment"}).get_text()
    print(link, product_title, product_review, price_original, installment, price_value)