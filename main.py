import random
import time
# Import the Label and Button objects
from objects.ui.Label import Label
from objects.ui.Button import Button
# Import the Spaceship
from objects.spaceships.Spaceship import Spaceship
# Import the game settings
import settings
from settings import *


def unpause() -> None:
    """
    Unpause the game.

    - paused: bool
        Ture/False, tells if the game is paused or not
    """
    global paused

    pygame.mouse.set_pos(mouse_position_backup)  # set the cursor position
    paused = False


def retry() -> None:
    """
    Reset the game and start over.

    - paused: bool
        True/False, tells if the game is paused or not
    - game_time: float
        Time when the game started
    - player_health_points: int
        Health points of the player
    - player_score: int
        Score of the player
    - player_sprite_group: pygame.sprite.GroupSingle
        A sprite group to manage the player
    - enemy_sprite_group: pygame.sprite.Group
        A sprite group to manage the enemies
    - last_beetle: float
        Time in seconds when the last Beetle was spawned
    - last_wasp: float
        Time in seconds when the last Wasp was spawned
    - last_queen: float
        Time in seconds when the last Queen was spawned
    """
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

    game_time = time.time()  # the get resets and so does the timer

    paused = False  # unpause the game


def draw_health() -> None:
    """
    Draw squares on screen depending on the amount of current health points of the player.

    - counter: int
        Used to add a space between the health point squares
    """

    counter = 0

    for hp in range(0, settings.player_health_points):
        # Draw a rectangle using pygame.draw.rect()
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((SCREEN_WIDTH - 35*counter) - 35, SCREEN_HEIGHT - 35, 25, 25))
        counter += 1


def spawner() -> None:
    """
    Create enemies depending on their set behavior in settings.enemy_behavior.

    - game_time: float
        The time when the game started
    - enemies: OrderedDict
        A dictionary with enemy information
    - scene_distance: int
        How far away from the screen the enemy must be spawned
    - time_now: float
         The time when this function is run
    - enemies["enemy"]: list
        The objects of all possible enemies: Beetle, Wasp, Queen
    - enemies["first_spawn"]: list
        A list of integers representing the number of seconds that have to pass in order to spawn the first
        enemy of that type
        The position of the integer corresponds to the position of the enemy in enemies["enemy"]
    - enemies["last_spawn"]: list
        A list of floats to store the time when the enemy was last spawned, it works together with enemies["frequency"]
        The position of the integer corresponds to the position of the enemy in enemies["enemy"]
    - enemies["frequency"]: list
        A list of integers representing the number of seconds to wait until another enemy of that type must
        be spawned
        The position of the integer corresponds to the position of the enemy in enemies["enemy"]
    """
    
    global game_time
    global enemies
    # The coordinate of y position, it helps draw the enemies out of the screen
    scene_distance = -50
    # Get the current time
    time_now = time.time()
    # Loop through the OrderedDict
    for c in range(len(enemies["enemy"])):
        # Check if the necessary amount of time for each type of enemy has passed so it can be spawned
        if time_now - game_time > enemies["first_spawn"][c]:
            if enemies["last_spawned"][c] == 0:  # check if it's the first spawn
                # Add a new enemy to the enemy_sprite_group with a random x position
                enemy_sprite_group.add(enemies["enemy"][c](random.randint(25, SCREEN_HEIGHT - 25), scene_distance))
                print("Spawned the first {}!".format(enemies["enemy"][c].__name__))
                enemies["last_spawned"][c] = time_now  # set the time when the last enemy of that type was spawned
            # Check if the necessary amount of time has passed since the last spawn
            elif time_now - enemies["last_spawned"][c] > enemies["frequency"][c]:
                # Add a new enemy to the enemy_sprite_group with a random x position
                enemy_sprite_group.add(enemies["enemy"][c](random.randint(25, SCREEN_HEIGHT - 25), scene_distance))
                print("Spawned another {}.".format(enemies["enemy"][c].__name__))
                enemies["last_spawned"][c] = time_now # set the time when the last enemy of that type was spawned


# Initialize the pygame module and pygame.mixer (for sounds)
pygame.init()
pygame.mixer.pre_init(44100, -16, 20)

# Set up the display window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # set the width and height
pygame.display.set_caption(SCREEN_TITLE)  # set the title

# Set up a pygame.time.Clock() object to control time and frame rate
clock = pygame.time.Clock()

# Set up the player by adding it to a pygame.sprite.GroupSingle()
# so it will be easier to update and manage
player_sprite_group.add(Spaceship())

# Store the enemy settings from settings.py
enemies = enemy_behavior

# Set up the background image and music
bkg_img = pygame.image.load(SCREEN_BKG_IMAGE).convert()
sound = pygame.mixer.Sound(settings.SOUNDS["background"])  # load the music
sound.set_volume(0.05)  # set the volume
sound.play(-1)  # play it indefinitely

# Create labels and buttons for the pause and retry menus
label_question = Label("", SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 100)  # create Label object
label_question.set_text_color((255, 255, 0))  # set its text color

button_ok = Button("OK", SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2, 150, 50)  # create Button object
button_ok.set_background_color((200, 200, 200))  # set its background color
button_ok.set_border_color((255, 255, 0))  # set its border color
button_ok.connect(unpause)  # connect to unpause, when clicked, call unpause()

button_quit = Button("QUIT", SCREEN_WIDTH//2 + 100, SCREEN_HEIGHT//2, 150, 50)  # create Button object
button_quit.set_background_color((200, 200, 200))  # set its background color
button_quit.set_border_color((255, 255, 0))  # set its border color
button_quit.connect(quit)  # connect to quit, when clicked, call quit()

button_retry = Button("RETRY", SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT//2, 150, 50)  # create Button object
button_retry.set_background_color((200, 200, 200))  # set its background color
button_retry.set_border_color((255, 255, 0))  # set its border color
button_retry.connect(retry)  # connect to retry, when clicked, call retry()

label_score = Label("", 60, SCREEN_HEIGHT - 15, 12)  # create Label object
label_score.set_text_color((255, 0, 0))  # set its text color

paused = False  # signal if the game is paused or not
running = True  # signal if the game is running or not

# Variable to store the position of the cursor to prevent cheating by pausing the game and moving the cursor around
mouse_position_backup = None

# Get the time when the game started
game_time = time.time()

# Enter the game loop
while running:
    """
    This is the main game loop, the objects are updated and drawn here.
    """
    screen.fill(SCREEN_BKG_COLOR)  # make the screen white
    screen.blit(bkg_img, (0, 0))  # on screen, draw the background image starting from (x=0, y=0) position

    draw_health()  # draw the current health of the player on the screen

    label_score.set_text(f"Score: {settings.player_score}")  # set the text of the label with the current score
    label_score.show(screen)  # display the label on the screen

    bullet_sprite_group.draw(screen)  # draw every Bullet() object stored in bullet_sprite_group
    enemy_sprite_group.draw(screen)  # draw every enemy(=Beetle, Wasp, Queen) object stored in enemy_sprite_group
    player_sprite_group.draw(screen)  # draw the player(=Player)

    for event in pygame.event.get():  # get events like key or mouse pressing
        if event.type == pygame.QUIT:  # check if the window's X button is clicked
            running = False  # set running to False, exit the loop and quit the game
        # Check if Escape key is pressed and if the player is alive
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and settings.player_health_points > 0:
            if paused:  # if the game is paused, then unpause it
                paused = False
                pygame.mouse.set_pos(mouse_position_backup)  # set the position of the mouse where it was before pause
            else:  # if the game is not paused, pause it
                paused = True
                mouse_position_backup = pygame.mouse.get_pos()  # get the position of the mouse
                pygame.mouse.set_pos(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.7)  # set the position of the mouse
    # If the game is not paused and the player is dead
    if settings.player_health_points < 1 and not paused:
        paused = True  # pause the game
        mouse_position_backup = pygame.mouse.get_pos()  # get the position of the mouse
        pygame.mouse.set_pos(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.7)  # set the position of the mouse
    # If the game is paused
    if paused:
        pygame.mouse.set_visible(True)  # make the cursor visible
        # Draw a transparent grey surface (it goes between the menu and the rest of the game objects)
        curtain = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))  # create the surface
        curtain.set_alpha(100)  # set the transparency
        screen.blit(curtain, (0, 0))  # draw it from (x=0, y=0) position

        if settings.player_health_points > 0:  # if the player is alive
            label_question.set_text("Paused. Do you wish to continue?")  # set the message of the label
            label_question.show(screen)  # display the label
            button_ok.show(screen)  # display an OK button
            button_quit.show(screen)  # display a QUIT button
        else:  # if the player is not alive
            player_sprite_group.update(screen)  # keep updating the player (so the explosion animation keeps running)
            enemy_sprite_group.update(screen)  # keep updating the enemy (so they still move on the screen)
            bullet_sprite_group.update()  # keep updating the remaining bullets

            label_question.set_text("You died! Retry?")  # set the message of the label
            label_question.show(screen)  # display the label
            button_retry.show(screen)  # display a RETRY button
            button_quit.show(screen)  # display a QUIT button
    # If the game is not paused
    if not paused:
        spawner()  # call spawner() to spawn enemies

        if settings.player_health_points > 0:  # if the player is alive,
            pygame.mouse.set_visible(False)  # hide the cursor

        player_sprite_group.update(screen)  # update the player
        enemy_sprite_group.update(screen)  # update the enemy
        bullet_sprite_group.update()  # update the bullets

    pygame.display.update()  # update the entire screen

    clock.tick(FRAME_RATE)  # limit the speed of the game using a set amount of frame rate

pygame.quit()  # close the module
quit()  # quit the program
