from ebook import EBook
from customer import Customer
from order import Order
from shopping_cart import ShoppingCart
from discount import Discount
from loyalty_program import LoyaltyProgram
from payment import Payment

# Create instances and simulate a purchase
ebook1 = EBook("Python Programming", "Author A", "2021-06-12", "Programming", 29.99)
customer = Customer("John Doe", "john@example.com", is_loyalty_member=True)
cart = ShoppingCart(customer)
cart.add_item(ebook1, 2)

# Generate an order and apply discounts
order = Order(customer, "2023-10-25")
order.add_ebook(ebook1)
loyalty_discount = LoyaltyProgram().apply_loyalty_discount(order.calculate_total_with_discount(0.1))

# Print objects
print(ebook1)
print(customer)
print(cart)
print(order)
print(f"Total after Loyalty Discount: ${loyalty_discount:.2f}")
