class Frame(object):
    """ A bike frame """
    def __init__(self):
        """
        Constructor
        """
        self.material = self.__class__.__name__[:-5]
        self.weight = self.WEIGHT
        self.cost = self.COST

class SteelFrame(Frame):
    """ A steel bike frame """
    COST = 25.0
    WEIGHT = 15.0

class AluminiumFrame(Frame):
    """ An aluminium bike frame """
    COST = 50.0
    WEIGHT = 6.0

class CarbonFrame(Frame):
    """ A carbon bike frame """
    COST = 200.0
    WEIGHT = 4.0

