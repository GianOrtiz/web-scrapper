from urllib.parse import urlparse
from typing import List
from bs4 import BeautifulSoup
from data.link.link_aggregator import LinkAggregator, Links

class MagazineLuizaLinkAggregator(LinkAggregator):
    def aggregate_links(self, content: LinkAggregator, page: str, links: Links):
        # MaganizeLuiza have some links with the relative path, so we must retrieve
        # the host to use as prefix to these links.
        url = urlparse(page)
        original_host = url.scheme + '://' + url.netloc
        page_links = content.find_all('a')
        for link in page_links:
            href = link.get('href')
            if href is not None:
                # Add the original host to the link if it does not have it.
                if original_host in href:
                    link_url = href
                else:
                    link_url = original_host + href
                links.append(link_url)
