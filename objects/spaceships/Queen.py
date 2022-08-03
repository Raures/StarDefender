from objects.spaceships.UFO import UFO


class Queen(UFO):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, r"imgs\Queen.png", 310, 175)

        self.health = 20
