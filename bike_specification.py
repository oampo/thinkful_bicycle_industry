class BikeSpecification(object):
    """ A specification for a bike """

    def __init__(self, name, manufacturer_name, frame_type, wheel_type):
        """
        Constructor

        Args:
            name: The name of the bike
            manufacturer_name: The name of the bike's manufacturer
            frame_type: The type of frame which the bike uses
            wheel_type: The type of wheel which the bike uses
        """
        self.name = name
        self.manufacturer_name = manufacturer_name
        self.frame_type = frame_type
        self.wheel_type = wheel_type

        self.cost = self.frame_type.COST + 2 * self.wheel_type.COST
        self.weight = self.frame_type.WEIGHT + 2 * self.wheel_type.WEIGHT

    def full_name(self):
        """
        Get the name of the bike including the manufacturer's name

        Returns:
            A string containing the full bike name
        """
        return "{} {}".format(self.manufacturer_name, self.name)
