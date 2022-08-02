import pygame

# Screen settings
SCREEN_TITLE = "Space Killing Spree"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN_BACKGROUND = (0, 0, 0)
FRAME_RATE = 60
FONT = r"fonts\PressStart2P.ttf"

# Player settings
player_sprite_group = pygame.sprite.GroupSingle()

bullet_sprite_group = pygame.sprite.Group()
player_score = 0
player_health_points = 3

# Enemy settings
enemy_sprite_group = pygame.sprite.Group()

first_beetle = 2
first_wasp = 5
first_queen = 15

last_beetle = 0
last_wasp = 0
last_queen = 0

beetle_frequency = 2
wasp_frequency = 4
queen_frequency = 20

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
