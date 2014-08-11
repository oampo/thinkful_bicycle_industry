from collections import defaultdict

class Shop(object):
    """ A bicycle shop """

    def __init__(self, name, markup):
        """
        Constructor

        Args:
            name: The name of the shop
            markup: The level of markup to apply to items.  A markup of 0.2 is
                equivalent to a 20% markup.
        """
        self.name = name
        self.markup = markup

        self.manufacturers = {}
        self.inventory = defaultdict(lambda: defaultdict(list))

        self.profit = 0

    def add_manufacturer(self, manufacturer):
        """
        Add products from a manufacturer to the shop's product range.

        Args:
            manufacturer: The manufacturer to stock
        """
        self.manufacturers[manufacturer.name] = manufacturer

    def buy(self, manufacturer_name, model_name):
        """
        Buy items from a manufacturer to add to the shop's inventory.

        Args:
            manufacturer_name: The manufacturer to purchase from
            model_name: The model to purchase
        """
        manufacturer = self.manufacturers[manufacturer_name]
        bike = manufacturer.sell(model_name)
        self.inventory[manufacturer_name][model_name].append(bike)

    def sell(self, manufacturer_name, model_name):
        """
        Sell an item from the shop's inventory.

        Args:
            manufacturer_name: The manufacturer of the item
            model_name: The model to sell
        """
        bike = self.inventory[manufacturer_name][model_name].pop()
        self.profit += (self.price(manufacturer_name, model_name) -
                        self.manufacturers[manufacturer_name].price(model_name))

        return bike

    def price(self, manufacturer_name, model_name):
        """
        Get the price of an item.

        Args:
            manufacturer_name: The name of the manufacturer of the item
            model_name: The model to find the price of

        Returns:
            The price of the item
        """
        manufacturer = self.manufacturers[manufacturer_name]
        return manufacturer.price(model_name) * (1.0 + self.markup)

    def stock(self, manufacturer_name, model_name):
        """
        Get the amount of stock of an item held

        Args:
            manufacturer_name: The name of the manufacturer of the item
            model_name: The model to find the stock level of

        Returns:
            The quantity of the item held in stock
        """
        return len(self.inventory[manufacturer_name][model_name])

    def product_range(self):
        """
        Get the definitions of all of the items for sale

        Returns:
            A list containing definitions for each item
        """
        product_range = []
        for manufacturer in self.manufacturers.itervalues():
            for model in manufacturer.models.itervalues():
                product_range.append(model)
        return product_range

