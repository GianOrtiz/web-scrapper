import re

from typing import List
from bs4 import BeautifulSoup
from data.link.link_aggregator import LinkAggregator, Links

class MercadoLivreLinkAggregator(LinkAggregator):
    def aggregate_links(self, content: LinkAggregator, page: str, links: Links):
        # Check if the pattern is a new page we want to access and it is not
        # one of the pages in the robots.txt.
        pattern = re.compile("https://lista\.mercadolivre\.com\.br/.*_[0-9]*_NoIndex_True|https://click1\.mercadolivre\.com\.br/.*|https://produto\.mercadolivre\.com\.br/.*")
        page_links = content.find_all('a') # Retrieve all a elements in the page.
        for link in page_links:
            # If the href of the element is not a noindex, we add it to the links list.
            href = link.get('href')
            if href is not None:
                if pattern.match(href) is not None and '/noindex/' not in href:
                    links.append(href)
