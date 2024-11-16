from urllib.parse import urlparse
from typing import List
from bs4 import BeautifulSoup
from data.link.link_aggregator import LinkAggregator, Links

class ZoomLinkAggregator(LinkAggregator):
    def aggregate_links(self, content: LinkAggregator, page: str, links: Links):
        # Zoom have some links with the relative path, so we must retrieve
        # the host to use as prefix to these links.
        url = urlparse(page)
        original_host = url.scheme + '://' + url.netloc
        page_links = content.find_all('a')
        for link in page_links:
            href = link.get('href')
            if href is not None:
                # We are interested in links with pages in Zoom only.
                if href.find('page=') > 0:
                    # Append the original host to the URLs.
                    link_url = original_host + href
                    links.append(link_url)
