import pygame

import settings


class Queen(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.image = pygame.Surface((310, 175)).convert_alpha()
        pygame.transform.scale(pygame.image.load(r"imgs\Queen.png").convert_alpha(), (310, 175), self.image)
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
        self.health = 20

    def update(self, screen):
        self.rect.y += self.speed

        if self.health == 0:

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
