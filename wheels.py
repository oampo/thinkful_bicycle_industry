class Wheel(object):
    """ A bike wheel """
    pass

class TimeTrialWheel(Wheel):
    """ A wheel for time-trial riding """
    name = "Time Trial Wheel"
    weight = 1.0
    cost = 125.0

class RoadWheel(Wheel):
    """ A wheel for road riding """
    name = "Road Wheel"
    weight = 1.0
    cost = 50.0

class MountainBikeWheel(Wheel):
    """ A wheel for mountain biking """
    name = "Mountain Bike Wheel"
    weight = 2.0
    cost = 50.0

