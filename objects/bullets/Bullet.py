import pygame

import settings


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.image = pygame.Surface((6, 31)).convert_alpha()
        pygame.transform.scale(pygame.image.load(r"imgs\BasicAttackBullet.png").convert_alpha(), (6, 31), self.image)
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

        self.sound = pygame.mixer.Sound(settings.hit_sound)
        self.sound.set_volume(0.4)

    def update(self):
        self.rect.y -= 20

        for sprite in settings.enemy_sprite_group:
            if self.rect.colliderect(sprite.rect) and sprite.health > 0:
                self.sound.play()
                if sprite.health - 1 == 0:
                    settings.player_score += 1

                sprite.health -= 1

                self.kill()

        if self.rect.y < -90:
            self.kill()
