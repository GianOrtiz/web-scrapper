

from typing import List
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from data.link.links import Links

class LinkAggregator(ABC):
    @abstractmethod
    def aggregate_links(self, content: BeautifulSoup, page: str, links: Links):
        return
