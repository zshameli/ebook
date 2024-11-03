from invoice import Invoice

class Order:
    """
    Class to represent an Order by a customer.
    """

    def __init__(self, customer, order_date):
        self.__order_date = order_date
        self.__total_amount = 0
        self.__ebooks = []
        self.__customer = customer
        self.invoice = None

    def add_ebook(self, ebook):
        self.__ebooks.append(ebook)
        self.__total_amount += ebook.price

    def calculate_total_with_discount(self, discount):
        return self.__total_amount * (1 - discount)

    def generate_invoice(self):
        self.invoice = Invoice(self.__order_date, self.__total_amount)

    def __str__(self):
        ebooks_list = ", ".join(str(ebook) for ebook in self.__ebooks)
        return f"Order(Date: {self.__order_date}, Total: ${self.__total_amount:.2f}, EBooks: [{ebooks_list}])"
