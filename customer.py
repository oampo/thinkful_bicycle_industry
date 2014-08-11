from errors import InsufficientFundsError

class Customer(object):
    """ A bike shop customer """

    def __init__(self, name, money):
        """
        Constructor

        Args:
            name: The name of the customer
            money: The amount of money the customer has to spend on a bike
        """
        self.name = name
        self.money = money
        self.bike = None

    def buy(self, shop, manufacturer, model):
        """
        Buy a bike from a shop

        Args:
            shop: A Shop object to buy the bike from
            manufacturer_name: The name of the bike's manufacturer
            model: The model to buy

        Raises:
            InsufficientFundsError: If not enough funds are available to buy
                the requested model
            KeyError: If the manufacturer or model of bike isn't sold by the
                shop
            IndexError: If the shop has no stock of the bike
        """
        if shop.price(manufacturer, model) > self.money:
            raise InsufficientFundsError("Insufficient funds")
        self.bike = shop.sell(manufacturer, model)
        self.money -= shop.price(manufacturer, model)

