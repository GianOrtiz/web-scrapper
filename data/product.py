from data.normalization.price import normalize_price
from data.normalization.installment import normalize_installment
from data.normalization.review import normalize_review

class Product:
    def __init__(self, link: str, title: str, review: str, price: str, installment: str):
        self.__link = link
        self.__title = title
        self.__review = normalize_review(review)
        self.__price = normalize_price(price)
        self.__installment = normalize_installment(installment)

    @property
    def link(self) -> str:
        return self.__link
    
    @property
    def title(self) -> str:
        return self.__title
    
    @property
    def review(self) -> str:
        return self.__review
    
    @property
    def price(self) -> str:
        return self.__price
    
    @property
    def installment(self) -> str:
        return self.__installment

    def to_json(self):
        return {
            'link': self.__link,
            'title': self.__title,
            'review': self.__review,
            'price': self.__price,
            'installment': self.__installment,
        }
