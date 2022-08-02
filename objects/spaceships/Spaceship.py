import pygame

from ..bullets.Bullet import Bullet
import settings


class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.x = 0
        self.y = 550

        self.image = pygame.Surface((45, 45)).convert_alpha()
        pygame.transform.scale(pygame.image.load(r"imgs\Defender.png").convert_alpha(), (45, 45), self.image)
        self.rect = self.image.get_rect(center=(self.x, self.y))

        self.fire_sound = pygame.mixer.Sound(settings.fire_sound)
        self.fire_sound.set_volume(0.1)

        self.destroyed_sound = pygame.mixer.Sound(settings.game_lost_sound)
        self.destroyed_sound.set_volume(1)

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

        self.fired = False

    def fire(self):
        self.fired = True
        self.fire_sound.play()
        settings.bullet_sprite_group.add(Bullet(self.rect.centerx, self.rect.centery))

    def update(self, screen):
        mouse = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0] and not self.fired:
            self.fire()
        elif not pygame.mouse.get_pressed()[0]:
            self.fired = False

        if settings.player_health_points < 1:
            if self.index > 10:
                self.kill()
            else:
                self.image = self.explosion_sprites[int(self.index)]
                self.rect = self.image.get_rect(center=self.rect.center)
                if self.index == 0:
                    self.destroyed_sound.play()
                self.index += 0.2
        else:
            self.rect.centerx = mouse[0]
