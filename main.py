import random
import time

from objects.ui.Label import Label
from objects.ui.Button import Button

from objects.spaceships.Spaceship import Spaceship

import settings
from settings import *


def unpause():
    global paused

    pygame.mouse.set_pos(mouse_position_backup)
    paused = False


def random_x_pos():
    return random.randint(25, SCREEN_WIDTH - 25)


def retry():
    global paused
    global game_time

    settings.player_health_points = 3
    settings.player_score = 0
    settings.player_sprite_group.add(Spaceship())

    settings.enemy_sprite_group.empty()
    settings.enemy_sprite_group.empty()
    settings.last_beetle = 0
    settings.last_wasp = 0
    settings.last_queen = 0

    game_time = time.time()

    paused = False


def draw_health():

    counter = 0

    for hp in range(0, settings.player_health_points):
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((SCREEN_WIDTH - 35 * counter) - 35, SCREEN_HEIGHT - 35, 25, 25))
        counter += 1


def spawner():
    global game_time
    global enemies

    scene_distance = -50

    time_now = time.time()

    for c in range(len(enemies["enemy"])):
        if time_now - game_time > enemies["first_spawn"][c]:
            if enemies["last_spawned"][c] == 0:
                enemy_sprite_group.add(enemies["enemy"][c](random_x_pos(), scene_distance))
                enemies["last_spawned"][c] = time_now
            elif time_now - enemies["last_spawned"][c] > enemies["frequency"][c]:
                enemy_sprite_group.add(enemies["enemy"][c](random_x_pos(), scene_distance))
                enemies["last_spawned"][c] = time_now


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)

game_time = time.time()

enemies = enemy_behavior

sound = pygame.mixer.Sound(settings.background_music)
sound.set_volume(0.05)
sound.play(-1)

clock = pygame.time.Clock()

label_question = Label("", SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 100)
label_question.set_text_color((255, 255, 0))

button_ok = Button("OK", SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2, 150, 50)
button_ok.set_background_color((200, 200, 200))
button_ok.set_border_color((255, 255, 0))
button_ok.connect(unpause)

button_quit = Button("QUIT", SCREEN_WIDTH//2 + 100, SCREEN_HEIGHT//2, 150, 50)
button_quit.set_background_color((200, 200, 200))
button_quit.set_border_color((255, 255, 0))
button_quit.connect(quit)

button_retry = Button("RETRY", SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT//2, 150, 50)
button_retry.set_background_color((200, 200, 200))
button_retry.set_border_color((255, 255, 0))
button_retry.connect(retry)

label_score = Label("", 60, SCREEN_HEIGHT - 15, 12)
label_score.set_text_color((255, 0, 0))

background_image = pygame.image.load(r"imgs\space_background.png").convert_alpha()

paused = False
running = True

mouse_position_backup = None

player_sprite_group.add(Spaceship())

while running:

    screen.fill((255, 255, 255))
    screen.blit(background_image, (0, 0))

    draw_health()

    label_score.set_text(f"Score: {settings.player_score}")
    label_score.show(screen)

    bullet_sprite_group.draw(screen)
    enemy_sprite_group.draw(screen)
    player_sprite_group.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and settings.player_health_points > 0:
            if paused:
                paused = False
                pygame.mouse.set_pos(mouse_position_backup)
            else:
                paused = True
                mouse_position_backup = pygame.mouse.get_pos()
                pygame.mouse.set_pos(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.7)

    if settings.player_health_points < 1 and not paused:
        paused = True
        mouse_position_backup = pygame.mouse.get_pos()
        pygame.mouse.set_pos(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.7)

    if paused:
        pygame.mouse.set_visible(True)

        curtain = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        curtain.set_alpha(100)
        screen.blit(curtain, (0, 0))

        if settings.player_health_points > 0:
            label_question.set_text("Paused. Do you wish to continue?")
            label_question.show(screen)
            button_ok.show(screen)
            button_quit.show(screen)
        else:
            player_sprite_group.update(screen)
            enemy_sprite_group.update(screen)
            bullet_sprite_group.update()

            label_question.set_text("You died! Retry?")
            label_question.show(screen)
            button_retry.show(screen)
            button_quit.show(screen)

    if not paused:
        spawner()

        if settings.player_health_points > 0:
            pygame.mouse.set_visible(False)

        player_sprite_group.update(screen)
        enemy_sprite_group.update(screen)
        bullet_sprite_group.update()

    pygame.display.update()

    clock.tick(FRAME_RATE)

pygame.quit()
quit()
