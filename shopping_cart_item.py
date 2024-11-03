class ShoppingCartItem:
    """
    Class to represent an Item in the Shopping Cart.
    """

    def __init__(self, ebook, quantity):
        self.__ebook = ebook
        self.__quantity = quantity

    @property
    def ebook(self):
        return self.__ebook

    @property
    def quantity(self):
        return self.__quantity

    def __str__(self):
        return f"ShoppingCartItem(EBook: {self.__ebook.title}, Quantity: {self.__quantity})"
