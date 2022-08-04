# Import base object
from objects.spaceships.UFO import UFO


class Wasp(UFO):
    """
    Create a Wasp object.

    Attributes
    ----------
    speed : int
        The speed of the Wasp
    health : int
        The health points of the Wasp
    strafe : bool
        True/False, allow the object to randomly change its position on the y-axis
    """
    def __init__(self, pos_x: int, pos_y: int):
        super().__init__(pos_x, pos_y, r"imgs\Wasp.png", 85, 25)
        """
        Parameters
        ----------
        pos_x : int
            The position of the object on the x-axis
        pos_y : int
            The position of the object on the y-axis
        """
        self.speed = 2
        self.health = 3
        self.strafe = True
