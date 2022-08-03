import pygame

from collections import OrderedDict

from objects.spaceships import Beetle, Wasp, Queen

# Screen settings
SCREEN_TITLE = "Space Killing Spree"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN_BACKGROUND = (0, 0, 0)
FRAME_RATE = 60
FONT = r"fonts\PressStart2P.ttf"

# Sound settings
SOUNDS_FOLDER_PATH = "sounds"
SOUNDS = {
  "hit": fr"{SOUNDS_PATH}\hit.wav",
  "fire": fr"{SOUNDS_PATH}\fire.wav",
  "game_lost": fr"{SOUNDS_PATH}\game_lost.wav",
  "lose_hp": fr"{SOUNDS_PATH}\lose_hp.wav",
  "enemy_destroyed": fr"{SOUNDS_PATH}\enemy_destroyed.wav",
  "background": fr"{SOUNDS_PATH}\land_of_8_bits.mp3"
}

# Player settings
player_sprite_group = pygame.sprite.GroupSingle()

bullet_sprite_group = pygame.sprite.Group()
player_score = 0
player_health_points = 3

# Enemy settings
enemy_sprite_group = pygame.sprite.Group()

enemy_behavior = OrderedDict()
enemy_behavior["enemy"] = [Beetle.Beetle, Wasp.Wasp, Queen.Queen]
enemy_behavior["first_spawn"] = [2, 5, 15]
enemy_behavior["last_spawned"] = [0, 0, 0]
enemy_behavior["frequency"] = [2, 4, 20]

# Sounds
# Hitting an enemy (Tribal dry drum):
# https://mixkit.co/free-sound-effects/tap/

# Destroying an enemy (Long pop):
# https://mixkit.co/free-sound-effects/pop/

# Destroying self (Retro arcade game over):
# https://mixkit.co/free-sound-effects/lose/

# Losing a life (Explainer video pops whoosh light pop):
# https://mixkit.co/free-sound-effects/pop/

# Firing (Beam 8):
# https://pixabay.com/sound-effects/search/laser/

# Background music (Land of 8 Bits):
# https://www.fesliyanstudios.com/royalty-free-music/downloads-c/8-bit-music/6

# Button hover (Button hover):
# https://freesound.org/people/Fachii/sounds/338229/

# Button clicked (UI button click 4/Typewriter soft click):
# https://www.zapsplat.com/sound-effect-category/button-clicks/
# https://mixkit.co/free-sound-effects/click/
"""
class UFO(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y, face):
		super().__init__()

		self.src = pygame.image.load(face).convert()
		self.image = pygame.Surface((self.src.get_width(), self.src.get_height())).convert_alpha()
		self.rect = self.image.get_rect(center=(pos_x, pos_y))

		self.center = None

		self.index = 0
		self.explosion_sprites = [WADWADAWDA]

		self.speed = 1
		self.health = 20

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
		if self.health == 0:
			self.explode()
		elif self.rect.y > pygame.display.get_surface().get_height():
			settings.player_health_points -= 1
			self.kill()			
		else:
			self.rect.y += self.speed
"""
