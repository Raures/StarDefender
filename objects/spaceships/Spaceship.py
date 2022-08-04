import pygame
# Import the Bullet object
from objects.bullets.Bullet import Bullet
# Import base object
from objects.spaceships.UFO import UFO
# Import the settings
import settings


class Spaceship(UFO):
    """
    Create a Spaceship object.

    This is class creates the player

    Attributes
    ----------
    fire_sound : pygame.mixer.Sound
        Set the sound to be played when shooting
    destroyed_sound : pygame.mixer.Sound
        Set the sound to be played when the player loses the game
    fired : bool
        True/False, keeps the shooting action to one per click

    Methods
    -------
    fire()
        Shoot
    update(screen)
        Update the state of the object
    """
    def __init__(self):
        super().__init__(0, 550, r"imgs\Defender.png", 45, 45)

        self.fire_sound = pygame.mixer.Sound(settings.SOUNDS["fire"])
        self.fire_sound.set_volume(0.1)

        self.destroyed_sound = pygame.mixer.Sound(settings.SOUNDS["game_lost"])
        self.destroyed_sound.set_volume(1)

        self.fired = False

    def fire(self) -> None:
        """
        Plays a sound and shoots a bullet
        """
        self.fired = True  # notice that the player shot
        self.fire_sound.play()  # play shoot sound
        # Add a Bullet object to the bullet_sprite_group
        settings.bullet_sprite_group.add(Bullet(self.rect.centerx, self.rect.centery))

    def update(self, screen) -> None:
        """
        Update the state of the player

        Parameters
        ----------
        screen : pygame.display.set_mode
            The surface object created by pygame
        """
        mouse = pygame.mouse.get_pos()  # get the position of the cursor
        # Check if the left mouse button is pressed and that the player is not currently shooting
        if pygame.mouse.get_pressed()[0] and not self.fired:
            self.fire()  # shoot
        elif not pygame.mouse.get_pressed()[0]:  # when the left mouse button is released
            self.fired = False  # notice that the player is not currently shooting
        # Check if the player is dead
        if settings.player_health_points < 1:
            # Destroy the object when there are no more explosion images to be displayer
            if self.index > len(self.explosion_sprites):
                self.kill()
            else:  # play the explosion animation
                self.image = self.explosion_sprites[int(self.index)]
                self.rect = self.image.get_rect(center=self.rect.center)
                if self.index == 0:  # play a sound when the explosion starts
                    self.destroyed_sound.play()
                self.index += 0.2  # increase the index by 0.2 to play the animation slower
        else:
            self.rect.centerx = mouse[0]  # set the center of the player to the position of the mouse on the x-axis
