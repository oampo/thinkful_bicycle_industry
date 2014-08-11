class Frame(object):
    """ A bike frame """
    pass

class SteelFrame(Frame):
    """ A steel bike frame """
    material = "Steel"
    cost = 25.0
    weight = 15.0

class AluminiumFrame(Frame):
    """ An aluminium bike frame """
    material = "Aluminium"
    cost = 50.0
    weight = 6.0

class CarbonFrame(Frame):
    """ A carbon bike frame """
    material = "Carbon Fibre"
    cost = 200.0
    weight = 4.0

