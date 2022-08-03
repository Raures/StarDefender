from objects.spaceships.UFO import UFO


class Beetle(UFO):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, r"imgs\Beetle.png", 35, 25)

        self.speed = 2
