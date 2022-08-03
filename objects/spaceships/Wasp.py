from objects.spaceships.UFO import UFO


class Wasp(UFO):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, r"imgs\Wasp.png", 85, 25)

        self.speed = 2
        self.health = 3
        self.strafe = True
