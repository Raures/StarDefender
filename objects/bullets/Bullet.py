import pygame
# Import the game settings
import settings


class Bullet(pygame.sprite.Sprite):
    """
    Create a Bullet object

    Attributes
    ----------
    image : pygame.Surface
        The surface of the object
    rect : pygame.Surface().get_rect
        The rectangle of the object
    sound : pygame.mixer.Sound
        The sound played when the bullet hits another object

    Methods
    -------
    update()
        Updates the state of the bullet
    """
    def __init__(self, pos_x: int, pos_y: int):
        super().__init__()
        """
        Parameters
        ----------
        pos_x : int
            The position of the bullet on the x-axis
        pos_y : int
            The position of the bullet on the y-axis
        """

        self.image = pygame.Surface((6, 31)).convert_alpha()
        pygame.transform.scale(pygame.image.load(r"imgs\BasicAttackBullet.png").convert_alpha(), (6, 31), self.image)
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

        self.sound = pygame.mixer.Sound(settings.SOUNDS["hit"])
        self.sound.set_volume(0.4)

    def update(self) -> None:
        """
        Update the state of the bullet.
        """
        self.rect.y -= 20  # move the bullet up the screen
        # Check if the bullet collides with any other object on the screen
        for sprite in settings.enemy_sprite_group:
            if self.rect.colliderect(sprite.rect) and sprite.health > 0:
                # If it does collide, play the hit sound
                self.sound.play()
                # If the bullet destroys the object, add +1 to the player's score
                if sprite.health - 1 == 0:
                    settings.player_score += 1
                # Decrease the health points of the object the bullet collides with
                sprite.health -= 1
                # Destroy the bullet
                self.kill()
        # If the bullet leaves the screen, destroy it
        if self.rect.y < -90:
            self.kill()
