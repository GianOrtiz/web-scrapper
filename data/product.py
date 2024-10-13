class Product:
    def __init__(self, link: str, title: str, review: str, price: str, installment: str):
        self.__link = link
        self.__title = title
        self.__review = review
        self.__price = price
        self.__installment = installment

    def to_json(self):
        return {
            'link': self.__link,
            'title': self.__title,
            'review': self.__review,
            'price': self.__price,
            'installment': self.__installment,
        }
