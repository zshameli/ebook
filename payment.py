class Payment:
    """
    Class to represent a Payment for an order.
    """

    def __init__(self, payment_date, payment_method, amount):
        self.__payment_date = payment_date
        self.__payment_method = payment_method
        self.__amount = amount

    def __str__(self):
        return f"Payment(Date: {self.__payment_date}, Method: {self.__payment_method}, Amount: ${self.__amount:.2f})"
