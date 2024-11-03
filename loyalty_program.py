class LoyaltyProgram:
    """
    Class to represent the Loyalty Program details.
    """

    def __init__(self, member_discount=0.10):
        self.__member_discount = member_discount

    def apply_loyalty_discount(self, total_amount):
        return total_amount * (1 - self.__member_discount)

    def __str__(self):
        return f"LoyaltyProgram(Discount: {self.__member_discount * 100}%)"
