from bike import Bike
from bike_specification import BikeSpecification


class Manufacturer(object):
    """ A manufacturer of bicycles """

    def __init__(self, name, markup):
        """
        Constructor

        Args:
            name: The name of the manufacturer
            markup: The level of markup to apply to bikes.  A markup of 0.2 is
                equivalent to a 20% markup.
        """
        self.name = name
        self.markup = markup
        self.models = {}

    def add_model(self, name, frame_type, wheel_type):
        """
        Add a new model to the manufacturer's bike range

        Args:
            name: The name of the model
            frame_type: The type of frame to use for the bike
            wheel_type: The type of wheel to use for the bike
        """
        specification = BikeSpecification(name, self.name, frame_type,
                                          wheel_type)
        self.models[name] = specification

    def price(self, model_name):
        """
        Get the price of a bike

        Args:
            model_name: The name of the model
        """
        return self.models[model_name].cost * (1 + self.markup)

    def sell(self, model_name):
        """
        Build and sell certain model of bike

        Args:
            model_name: The name of the model

        Returns:
            A Bike object
        """
        specification = self.models[model_name]
        bike = Bike(specification)
        return bike

