# Import base object
from objects.spaceships.UFO import UFO


class Beetle(UFO):
    """
    Create a Beetle object.

    Attributes
    ----------
    speed : int
        The speed of the Beetle
    """
    def __init__(self, pos_x: int, pos_y: int):
        super().__init__(pos_x, pos_y, r"imgs\Beetle.png", 35, 25)
        """
        Parameters
        ----------
        pos_x : int
            The position of the object on the x-axis
        pos_y : int
            The position of the object on the y-axis
        """
        self.speed = 2
