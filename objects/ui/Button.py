import pygame

from settings import FONT


class Button:
    def __init__(self, text, pos_x, pos_y, width, height):

        self.text = text
        self.text_size = 15
        self.text_font = FONT
        self.text_color = (0, 0, 0)

        self.x = pos_x
        self.y = pos_y

        self.width = width
        self.height = height

        self.background_color = (0, 255, 255)
        self.background_surface = None
        self.background_rectangle = None

        self.border = True
        self.border_color = (0, 255, 0)
        self.border_thickness = 5

        # mouse events
        self.already_clicked = False
        self.click_reaction = None

    def set_text(self, new_text):
        self.text = new_text

    def set_text_size(self, new_size):
        self.text_size = new_size

    def set_text_font(self, new_font):
        self.text_font = new_font

    def set_text_color(self, new_color):
        self.text_color = new_color

    def set_position(self, new_x, new_y):
        if new_x:
            self.x = new_x
        if new_y:
            self.y = new_y

    def set_size(self, new_width, new_height):
        if new_width:
            self.width = new_width
        if new_height:
            self.height = new_height

    def set_background_color(self, new_color):
        self.background_color = new_color

    def set_border_color(self, new_color):
        self.border_color = new_color

    def set_border_thickness(self, new_thickness):
        self.border_thickness = new_thickness

    def hover(self):
        if self.background_rectangle.collidepoint(pygame.mouse.get_pos()):
            return True
        else:
            return False

    def clicked(self):
        if self.hover() and pygame.mouse.get_pressed()[0] and not self.already_clicked:
            if self.click_reaction is not None:
                self.click_reaction()

            self.already_clicked = True

        elif not pygame.mouse.get_pressed()[0]:
            self.already_clicked = False

    def connect(self, func):
        self.click_reaction = func

    def show(self, surface):

        text_surface = pygame.font.Font(self.text_font, self.text_size).render(self.text, True, self.text_color)
        text_rectangle = text_surface.get_rect(center=(self.x, self.y))

        self.background_surface = pygame.Surface((self.width, self.height))
        self.background_surface.fill(self.background_color)
        self.background_rectangle = self.background_surface.get_rect(center=(self.x, self.y))

        self.clicked()

        surface.blit(self.background_surface, self.background_rectangle)

        if self.hover():
            pygame.draw.rect(surface, self.border_color, pygame.Rect(pygame.Surface((self.width, self.height)).get_rect(center=(self.x, self.y))),  self.border_thickness)

        surface.blit(text_surface, text_rectangle)
