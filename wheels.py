class Wheel(object):
    """ A bike wheel """
    def __init__(self):
        """
        Constructor
        """
        self.name = self.__class__.__name__[:-5]
        self.weight = self.WEIGHT
        self.cost = self.COST

class TimeTrialWheel(Wheel):
    """ A wheel for time-trial riding """
    WEIGHT = 1.0
    COST = 125.0

class RoadWheel(Wheel):
    """ A wheel for road riding """
    WEIGHT = 1.0
    COST = 50.0

class MountainBikeWheel(Wheel):
    """ A wheel for mountain biking """
    WEIGHT = 2.0
    COST = 50.0

