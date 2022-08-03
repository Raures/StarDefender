import pygame

from time import time
from random import randint

import settings


class UFO(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, face, w, h):
        super().__init__()

        self.src = pygame.image.load(face).convert_alpha()
        self.image = pygame.Surface((w, h)).convert_alpha()
        pygame.transform.scale(self.src.convert_alpha(), (w, h), self.image)
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

        self.damage_sound = pygame.mixer.Sound(settings.SOUNDS["hit"])
        self.destroyed_sound = pygame.mixer.Sound(settings.SOUNDS["enemy_destroyed"])

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

    def strafing(self):
        if self.strafe and self.health > 0:
            if time() - self.timer > self.cooldown and randint(0, 100) < self.chance_to_strafe:
                if self.direction == 1:
                    self.rect.x += 50
                else:
                    self.rect.x -= 50

                self.direction = randint(0, 1)
                self.timer = time()

            if self.health > 0 and self.rect.x + self.rect.width > settings.SCREEN_WIDTH:
                self.rect.x = settings.SCREEN_WIDTH - self.rect.width - 10
            elif self.health > 0 > self.rect.x - 5:
                self.rect.x = 10

    def explode(self):
        self.speed = 0
        self.center = self.rect.center

        if self.index > len(self.explosion_sprites):
            self.kill()
        else:
            self.image = self.explosion_sprites[int(self.index)]
            self.rect = self.image.get_rect(center=self.center)
            self.index += 0.2

    def update(self, screen):
        self.strafing()
        if self.health == 0:
            self.explode()
        elif self.rect.y > pygame.display.get_surface().get_height():
            settings.player_health_points -= 1
            self.kill()
        else:
            self.rect.y += self.speed
