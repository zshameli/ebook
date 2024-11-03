import unittest
from ebook import EBook
from customer import Customer
from order import Order
from shopping_cart import ShoppingCart
from shopping_cart_item import ShoppingCartItem
from discount import Discount
from invoice import Invoice
from loyalty_program import LoyaltyProgram
from payment import Payment

class TestEBookStore(unittest.TestCase):
    
    def setUp(self):
        # Initialize common test objects used across multiple test cases
        self.ebook1 = EBook("Python Programming", "Author A", "2021-06-12", "Programming", 29.99)
        self.ebook2 = EBook("Data Science Fundamentals", "Author B", "2020-01-20", "Data Science", 39.99)
        self.customer = Customer("John Doe", "john@example.com", is_loyalty_member=True)
        self.cart = ShoppingCart(self.customer)
        self.order = Order(self.customer, "2023-10-25")

    def test_add_ebook_to_catalog(self):
        """Test adding an e-book to the catalog"""
        self.assertEqual(self.ebook1.title, "Python Programming")
        self.assertEqual(self.ebook1.price, 29.99)

    def test_modify_ebook_details(self):
        """Test modifying details of an e-book"""
        self.ebook1.price = 24.99  # modifying price with setter
        self.assertEqual(self.ebook1.price, 24.99)

    def test_remove_ebook(self):
        """Test removing an e-book from the catalog (simulation by deleting object)"""
        ebook = EBook("Sample Book", "Author C", "2021-01-01", "Sample Genre", 19.99)
        del ebook  # deleting the ebook object
        with self.assertRaises(NameError):
            print(ebook)  # accessing after deletion should raise NameError

    def test_add_customer_account(self):
        """Test adding a new customer account"""
        new_customer = Customer("Alice Smith", "alice@example.com")
        self.assertEqual(new_customer.name, "Alice Smith")
        self.assertFalse(new_customer.is_loyalty_member)

    def test_modify_customer_account(self):
        """Test modifying customer account details"""
        self.customer.is_loyalty_member = False
        self.assertFalse(self.customer.is_loyalty_member)

    def test_add_ebook_to_shopping_cart(self):
        """Test adding e-books to the shopping cart"""
        self.cart.add_item(self.ebook1, 2)
        self.assertEqual(len(self.cart._ShoppingCart__items), 1)  # One item added
        self.assertEqual(self.cart._ShoppingCart__items[0].quantity, 2)

    def test_remove_item_from_cart(self):
        """Test removing items from the shopping cart"""
        self.cart.add_item(self.ebook1, 1)
        self.cart._ShoppingCart__items.pop(0)  # remove the item
        self.assertEqual(len(self.cart._ShoppingCart__items), 0)

    def test_apply_loyalty_discount(self):
        """Test applying loyalty discount to an order"""
        self.order.add_ebook(self.ebook1)
        loyalty_discounted_total = LoyaltyProgram().apply_loyalty_discount(self.order.calculate_total_with_discount(0))
        expected_total = self.ebook1.price * 0.9  # 10% loyalty discount applied
        self.assertAlmostEqual(loyalty_discounted_total, expected_total)

    def test_bulk_purchase_discount(self):
        """Test applying a bulk discount for 8 or more e-books in a single order"""
        for _ in range(8):
            self.order.add_ebook(self.ebook1)
        total_with_bulk_discount = self.order.calculate_total_with_discount(0.2)
        expected_total = 8 * self.ebook1.price * 0.8  # 20% off bulk purchase
        self.assertAlmostEqual(total_with_bulk_discount, expected_total)

    def test_invoice_generation(self):
        """Test the generation of an invoice with discounts applied"""
        self.order.add_ebook(self.ebook1)
        self.order.add_ebook(self.ebook2)
        self.order.generate_invoice()
        self.assertIsInstance(self.order.invoice, Invoice)
        self.assertAlmostEqual(self.order.invoice._Invoice__invoice_total, 69.98)

    def test_payment_processing(self):
        """Test payment processing for an order"""
        payment = Payment("2023-10-25", "Credit Card", 69.98)
        self.assertEqual(payment._Payment__amount, 69.98)
        self.assertEqual(payment._Payment__payment_method, "Credit Card")

    def test_discount_application(self):
        """Test the application of discounts"""
        discount = Discount("Loyalty Discount", 0.1)
        discounted_total = discount.apply_discount(100.0)
        self.assertAlmostEqual(discounted_total, 90.0)  # 10% off

    def test_cart_total_amount(self):
        """Test calculation of the total amount in the cart before checkout"""
        self.cart.add_item(self.ebook1, 2)
        total_amount = sum(item.ebook.price * item.quantity for item in self.cart._ShoppingCart__items)
        self.assertAlmostEqual(total_amount, 59.98)  # 2 copies of ebook1 at 29.99 each


if __name__ == "__main__":
    unittest.main()
