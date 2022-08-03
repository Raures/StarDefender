import pygame

from collections import OrderedDict

from objects.spaceships.Beetle import Beetle
from objects.spaceships.Wasp import Wasp
from objects.spaceships.Queen import Queen

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
  "hit": fr"{SOUNDS_FOLDER_PATH}\hit.wav",
  "fire": fr"{SOUNDS_FOLDER_PATH}\fire.wav",
  "game_lost": fr"{SOUNDS_FOLDER_PATH}\game_lost.wav",
  "lose_hp": fr"{SOUNDS_FOLDER_PATH}\lose_hp.wav",
  "enemy_destroyed": fr"{SOUNDS_FOLDER_PATH}\enemy_destroyed.wav",
  "background": fr"{SOUNDS_FOLDER_PATH}\land_of_8_bits.mp3"
}

# Player settings
player_sprite_group = pygame.sprite.GroupSingle()

bullet_sprite_group = pygame.sprite.Group()
player_score = 0
player_health_points = 3

# Enemy settings
enemy_sprite_group = pygame.sprite.Group()

enemy_behavior = OrderedDict()
enemy_behavior["enemy"] = [Beetle, Wasp, Queen]
enemy_behavior["first_spawn"] = [2, 5, 15]
enemy_behavior["last_spawned"] = [0, 0, 0]
enemy_behavior["frequency"] = [2, 4, 20]

# Button hover (Button hover):
# https://freesound.org/people/Fachii/sounds/338229/

# Button clicked (UI button click 4/Typewriter soft click):
# https://www.zapsplat.com/sound-effect-category/button-clicks/
# https://mixkit.co/free-sound-effects/click/
