"""Module which implements the classes needed for evaluating the
glass traingle problem
"""

import decimal

class Glass():
    """ A simple class representing a glass in the triangle
    """

    def __init__(self, vertical_position, horizontal_position, max_capacity):
        """
        Initialize the object with its position in the stack and it's maximum capacity
        :param vertical_position: Index of the row where this glass is in the triangle
        :param horizontal_position: Index of the position in the row
        :param max_capacity: Maximum capacity of this glass
        """

        if horizontal_position < 0:
            raise IndexError(f'Vertical position {vertical_position} can not be negative.')

        if vertical_position < 0:
            raise IndexError(f'Horizontal position {horizontal_position} can not be negative.')

        if max_capacity < 0:
            raise IndexError(f'Maximum capacity of a glass {max_capacity} must be positive.')

        self.vertical_position = vertical_position
        self.horizontal_position = horizontal_position
        self.max_capacity = max_capacity
        self.current_volume = 0

    @property
    def percentage_full(self):
        """Method to determine the percentage is the glass full.
        Decimal places are truncated to 4 decimal places
        :return: Decimal
        """
        return self.percent_full * 100

    @property
    def percent_full(self):
        """Method to determine how much percent is the glass full.
        Decimal places are truncated to 4 decimal places
        :return: Decimal
        """
        filled = decimal.Decimal(self.current_volume / self.max_capacity)
        percent_full = decimal.Decimal(filled).quantize(decimal.Decimal('.001'), rounding=decimal.ROUND_DOWN)
        return decimal.Decimal(percent_full)

    def get_graph_node_string(self):
        """Returns a graph node friendly representation of the glass
        :return: str
        """
        return str(f'i = {self.vertical_position} j = {self.horizontal_position}\n'
                   f'{self.current_volume} ml\n'
                   f'{(self.percentage_full)}% full'.encode('utf-8'))

    def get_node_fill_color(self):
        """Get color for node based on perfect full
        :return:
        """
        if self.percent_full.compare(0) == 0:
            return f'"white"'

        return f'"white:blue;{self.percent_full}"'

    def __str__(self):
        """Returns a user friendly representation of the glass
        :return: str
        """
        return str(f'{self.vertical_position},{self.horizontal_position} | '
                   f'{self.current_volume} ml | '
                   f'{(self.percentage_full)}% full')

    def __repr__(self):
        """Returns a user friendly representation of the glass
        :return: str
        """
        return self.__str__()
