class Bike(object):
    """ A bike """

    def __init__(self, specification):
        """
        Constructor

        Args:
            specification: A Specification object for the bike to follow
        """
        self.name = specification.name
        self.manufacturer_name = specification.manufacturer_name

        self.frame = specification.frame_type()
        self.front_wheel = specification.wheel_type()
        self.back_wheel = specification.wheel_type()

        self.cost = specification.cost
        self.weight = specification.weight

    def full_name(self):
        """
        Get the name of the bike including the manufacturer's name

        Returns:
            A string containing the full bike name
        """
        return "{} {}".format(self.manufacturer_name, self.name)
