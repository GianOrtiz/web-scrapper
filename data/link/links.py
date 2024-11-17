from typing import List
from random import shuffle

class Links:
    def __init__(self, links: List[str]):
        # We make three lists for every implementation we have so we can
        # evenly distribute access tot he links.
        self.__mercadolivre_links: List[str] = []
        self.__zoom_links: List[str] = []
        self.__magazineluiza_links: List[str] = []
        self.__list_to_access = 0
        for link in links:
            if 'magazineluiza' in link:
                self.__magazineluiza_links.append(link)
            elif 'zoom' in link:
                self.__zoom_links.append(link)
            elif 'mercadolivre' in link:
                self.__mercadolivre_links.append(link)
        self.__links_accessed: List[str] = []

    def append(self, link: str):
        # Do not append the link if it is already accessed earlier.
        if link in self.__magazineluiza_links or link in self.__zoom_links or link in self.__mercadolivre_links or link in self.__links_accessed:
            return

        # Ignores blogs and social medias.
        if 'instagram' in link or 'blog' in link or 'facebook' in link or 'linkedin' in link:
            return

        # Append the link to the correct implementation list.
        if 'magazineluiza' in link:
            self.__magazineluiza_links.append(link)
        elif 'zoom' in link:
            self.__zoom_links.append(link)
        elif 'mercadolivre' in link:
            self.__mercadolivre_links.append(link)

        # Shuffles all list to distribute access to links.
        self.shuffle()

    def pop(self) -> str:
        # Select the correct list to access.
        if self.__list_to_access == 0:
            links_list = self.__magazineluiza_links
        elif self.__list_to_access == 1:
            links_list = self.__mercadolivre_links
        elif self.__list_to_access == 2:
            links_list = self.__zoom_links

        self.__list_to_access = (self.__list_to_access + 1) % 3 # Increase the next list to access.
        if len(links_list) == 0: # When the list is exhausted uses other list.
            link = self.pop()
        else:
            link = links_list.pop()
            self.__links_accessed.append(link)

        return link
    
    def shuffle(self):
        shuffle(self.__magazineluiza_links)
        shuffle(self.__zoom_links)
        shuffle(self.__mercadolivre_links)
