class Invoice:
    """
    Class to represent an Invoice generated from an Order.
    """

    def __init__(self, invoice_date, invoice_total):
        self.__invoice_date = invoice_date
        self.__invoice_total = invoice_total

    def __str__(self):
        return f"Invoice(Date: {self.__invoice_date}, Total: ${self.__invoice_total:.2f})"
