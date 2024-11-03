class EBook:
    """
    Class to represent an EBook in the store catalog.

    Attributes:
        title (str): The title of the e-book.
        author (str): The author of the e-book.
        publication_date (str): The publication date of the e-book.
        genre (str): The genre of the e-book.
        price (float): The price of the e-book.
    """

    def __init__(self, title, author, publication_date, genre, price):
        """
        Initializes an instance of the EBook class with given attributes.

        Args:
            title (str): The title of the e-book.
            author (str): The author of the e-book.
            publication_date (str): The publication date of the e-book.
            genre (str): The genre of the e-book.
            price (float): The price of the e-book.
        """
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date
        self.__genre = genre
        self.__price = price

    # Getters
    @property
    def title(self):
        """Gets the title of the e-book."""
        return self.__title

    @property
    def author(self):
        """Gets the author of the e-book."""
        return self.__author

    @property
    def publication_date(self):
        """Gets the publication date of the e-book."""
        return self.__publication_date

    @property
    def genre(self):
        """Gets the genre of the e-book."""
        return self.__genre

    @property
    def price(self):
        """Gets the price of the e-book."""
        return self.__price

    # Setters
    @title.setter
    def title(self, new_title):
        """Sets a new title for the e-book."""
        self.__title = new_title

    @price.setter
    def price(self, new_price):
        """Sets a new price for the e-book."""
        if new_price < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = new_price

    # String representation
    def __str__(self):
        """
        Returns a string representation of the EBook instance.

        Returns:
            str: A formatted string with e-book details.
        """
        return (f"EBook(Title: {self.__title}, Author: {self.__author}, "
                f"Publication Date: {self.__publication_date}, Genre: {self.__genre}, "
                f"Price: ${self.__price:.2f})")

    # Method to display full details as a dictionary (optional)
    def get_details(self):
        """
        Returns all details of the e-book as a dictionary.

        Returns:
            dict: A dictionary with all e-book details.
        """
        return {
            "Title": self.__title,
            "Author": self.__author,
            "Publication Date": self.__publication_date,
            "Genre": self.__genre,
            "Price": self.__price
        }
