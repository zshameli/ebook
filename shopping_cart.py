from shopping_cart_item import ShoppingCartItem

class ShoppingCart:
    """
    Class to represent a Shopping Cart.
    """

    def __init__(self, customer):
        self.__customer = customer
        self.__items = []

    def add_item(self, ebook, quantity=1):
        item = ShoppingCartItem(ebook, quantity)
        self.__items.append(item)

    def __str__(self):
        items_list = ", ".join(str(item) for item in self.__items)
        return f"ShoppingCart(Customer: {self.__customer.name}, Items: [{items_list}])"
