import pygame

from time import time
from random import randint
# Import the settings
import settings


class UFO(pygame.sprite.Sprite):
    """
    Base class for spaceships.

    Attributes
    ----------
    src : image
        The image of the object
    image : pygame.Surface
        The surface of the object
    rect : pygame.Surface().get_rect
        The rectangle of the object
    damage_sound : pygame.mixer.Sound
        The sound when the object is hit by Bullet
    destroyed_sound : pygame.mixer.Sound
        The sound when the object health points reach 0
    lose_hp_sound : pygame.mixer.Sound
        The sound when the player loses hp
    center : tuple
        Integers representing the position of the center of the object
    index : int
        Integer to keep track of the current explosion image
    explosion_sprites : list
        Images of explosion
    speed : int
        The speed of the object
    health : int
        The health of the object
    strafe : bool
        True/False, allows the object to randomly change its position on the y-axis
    cooldown : float
        The amount of time to wait between strafes
    timer : float
        The time when the object was created
    chance_to_strafe : int
        The chance of the object to strafe
    direction : bool
        The direction of the strafe

    Methods
    -------
    strafing()
        Randomly changes the position of the object on the y-axis
    explode()
        Displays an explosion animation
    update(screen)
        Updates the object
    """
    def __init__(self, pos_x, pos_y, face, w, h):
        super().__init__()
        """
        Parameters
        ----------
        pos_x : int
            The position on the x-axis
        pos_y : int
            The position on the y-axis
        face : str
            Path to the image of the object
        w : int
            Width of the object
        h : int
            Height of the object
        """

        self.src = pygame.image.load(face).convert_alpha()
        self.image = pygame.Surface((w, h)).convert_alpha()
        pygame.transform.scale(self.src.convert_alpha(), (w, h), self.image)
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

        self.damage_sound = pygame.mixer.Sound(settings.SOUNDS["hit"])
        self.destroyed_sound = pygame.mixer.Sound(settings.SOUNDS["enemy_destroyed"])
        self.lose_hp_sound = pygame.mixer.Sound(settings.SOUNDS["lose_hp"])
        self.lose_hp_sound.set_volume(0.5)

        self.center = None

        self.index = 0
        self.explosion_sprites = []
        self.explosion_sprites.append(pygame.image.load(r"imgs\Explosion1_1.png"))
        self.explosion_sprites.append(pygame.image.load(r"imgs\Explosion1_2.png"))
        self.explosion_sprites.append(pygame.image.load(r"imgs\Explosion1_3.png"))
        self.explosion_sprites.append(pygame.image.load(r"imgs\Explosion1_4.png"))
        self.explosion_sprites.append(pygame.image.load(r"imgs\Explosion1_5.png"))
        self.explosion_sprites.append(pygame.image.load(r"imgs\Explosion1_6.png"))
        self.explosion_sprites.append(pygame.image.load(r"imgs\Explosion1_7.png"))
        self.explosion_sprites.append(pygame.image.load(r"imgs\Explosion1_8.png"))
        self.explosion_sprites.append(pygame.image.load(r"imgs\Explosion1_9.png"))
        self.explosion_sprites.append(pygame.image.load(r"imgs\Explosion1_10.png"))
        self.explosion_sprites.append(pygame.image.load(r"imgs\Explosion1_11.png"))

        self.speed = 1
        self.health = 1

        self.strafe = False
        self.cooldown = 1.75
        self.timer = time()
        self.chance_to_strafe = 25
        self.direction = randint(0, 1)

    def strafing(self) -> None:
        """
        Randomly changes the position of the object on the y-axis.
        """
        # Check if the object can strafe and it's alive
        if self.strafe and self.health > 0:
            # Check if enough time has passed and try to strafe
            if time() - self.timer > self.cooldown and randint(0, 100) < self.chance_to_strafe:
                # Get the strafe direction
                if self.direction == 1:
                    self.rect.x += 50
                else:
                    self.rect.x -= 50
                # Get a new strafe direction
                self.direction = randint(0, 1)
                self.timer = time()  # reset the timer
            # Forbid the object to leave the screen
            if self.rect.x + self.rect.width > settings.SCREEN_WIDTH:
                self.rect.x = settings.SCREEN_WIDTH - self.rect.width - 10
            elif self.rect.x - 5:
                self.rect.x = 10

    def explode(self) -> None:
        """
        Display an explosion animation when the object is dead.

        """
        # Prevent the player from moving
        self.speed = 0
        self.center = self.rect.center  # get the center of the object to display each explosion frame in the same pos
        # Check if all explosion images have been displayed
        if self.index > len(self.explosion_sprites):
            self.kill()  # destroy the object
        else:
            self.image = self.explosion_sprites[int(self.index)]  # display the current explosion image
            self.rect = self.image.get_rect(center=self.center)
            self.index += 0.2

    def update(self, screen) -> None:
        """
        Update the object.

        Parameters
        ----------
        screen : pygame.display.set_mode()
            The screen object created by pygame
        """
        # Check if the object can strafe and strafe
        self.strafing()
        # Check if the object is dead and start the exploding animation
        if self.health == 0:
            self.explode()
        # If the object manages to leave the screen, decrease player's health points by 1 and kill this object
        elif self.rect.y > pygame.display.get_surface().get_height():
            settings.player_health_points -= 1
            self.lose_hp_sound.play()  # play lose hp sound
            self.kill()
        else:
            self.rect.y += self.speed  # Move the object downwards
