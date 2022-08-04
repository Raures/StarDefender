# Import base object
from objects.spaceships.UFO import UFO


class Queen(UFO):
    """
    Create a Queen object.

    Attributes
    ----------
    health : int
        The health points of the Queen
    """
    def __init__(self, pos_x: int, pos_y: int):
        super().__init__(pos_x, pos_y, r"imgs\Queen.png", 310, 175)
        """
        Parameters
        ----------
        pos_x : int
            The position of the object on the x-axis
        pos_y : int
            The position of the object on the y-axis
        """
        self.health = 20
