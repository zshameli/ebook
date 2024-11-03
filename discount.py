class Discount:
    """
    Class to represent discounts applied on an order.
    """

    def __init__(self, discount_type, discount_value):
        self.__discount_type = discount_type
        self.__discount_value = discount_value

    def apply_discount(self, total_amount):
        return total_amount * (1 - self.__discount_value)

    def __str__(self):
        return f"Discount(Type: {self.__discount_type}, Value: {self.__discount_value * 100}%)"
