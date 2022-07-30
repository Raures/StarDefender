import pygame
import random
import time

import settings


class Wasp(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.image = pygame.Surface((85, 25)).convert_alpha()
        pygame.transform.scale(pygame.image.load(r"imgs\Wasp.png").convert_alpha(), (85, 25), self.image)
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

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
        self.health = 3
        self.cooldown = 1.75
        self.timer = time.time()
        self.chance_to_strafe = 25
        self.direction = random.randint(0, 1)

    def update(self, screen):
        self.rect.y += self.speed

        if self.health != 0:
            if time.time() - self.timer > self.cooldown and random.randint(0, 100) < self.chance_to_strafe:
                if self.direction == 1:
                    self.rect.x += 50
                else:
                    self.rect.x -= 50

                self.direction = random.randint(0, 1)
                self.timer = time.time()

            if self.health > 0 and self.rect.x + self.rect.width > settings.SCREEN_WIDTH:
                self.rect.x = settings.SCREEN_WIDTH - self.rect.width - 10
            elif self.health > 0 and self.rect.x - 5 < 0:
                self.rect.x = 10

        elif self.health == 0:

            self.speed = 0
            self.center = self.rect.center

            if self.index > 10:
                self.kill()
            else:
                self.image = self.explosion_sprites[int(self.index)]
                self.rect = self.image.get_rect(center=self.center)
                self.index += 0.2

        if self.rect.y > pygame.display.get_surface().get_height():
            settings.player_health_points -= 1
            self.kill()
