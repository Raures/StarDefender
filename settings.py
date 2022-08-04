import pygame

from collections import OrderedDict
# Import enemy objects
from objects.spaceships.Beetle import Beetle
from objects.spaceships.Wasp import Wasp
from objects.spaceships.Queen import Queen

# Screen settings
SCREEN_TITLE = "Star Defender"  # title of the screen
SCREEN_WIDTH = 800  # width of the screen
SCREEN_HEIGHT = 600  # height of the screen
SCREEN_BKG_COLOR = (0, 0, 0)  # the background color
SCREEN_BKG_IMAGE = r"imgs\Background.png"  # the background image
FRAME_RATE = 60  # set the screen frame rate
FONT = r"fonts\PressStart2P.ttf"  # set a global font for the game text

# Sound settings
SOUNDS_FOLDER_PATH = "sounds"  # points to the folder containing sounds
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
player_score = 0
player_health_points = 3

# Bullet settings
bullet_sprite_group = pygame.sprite.Group()

# Enemy settings
enemy_sprite_group = pygame.sprite.Group()

enemy_behavior = OrderedDict()
enemy_behavior["enemy"] = [Beetle, Wasp, Queen]
enemy_behavior["first_spawn"] = [2, 5, 15]
enemy_behavior["last_spawned"] = [0, 0, 0]
enemy_behavior["frequency"] = [2, 4, 20]
