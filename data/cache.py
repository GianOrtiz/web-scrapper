import requests
import os.path
import typing

from datetime import datetime
from hashlib import sha256

class Cache:
    def __init__(self, location: str):
        self.__location: str = location

    def get_page(self, page: str) -> typing.Tuple[bytes, bool] :
        h = sha256(page.encode()).hexdigest()
        now = datetime.now()
        date = str(now.day) + '-' + str(now.month) + '-' + str(now.year)
        path = self.__location + '/' + date
        path_exists = os.path.isdir(path)
        if not path_exists:
            os.mkdir(path)
        path += '/' + h
        cache_hit = os.path.isfile(path)
        if cache_hit:
            with open(path, 'r') as file:
                content = file.read()
                return content, True
    
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
            "Accept-Encoding": "gzip, deflate, br", 
	        "Accept-Language": "en-US,en;q=0.9", 
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        }
        try:
            page_request = requests.get(page, headers=headers)
            content = page_request.content
            with open(path, 'w+') as f:
                f.write(content.decode('utf-8'))
            return content, False
        # Workaround when the URL is bad formatted.
        except:
            return '', True
        