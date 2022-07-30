import pygame

from settings import FONT


class Label:
    def __init__(self, text: str,
                 pos_x: int,
                 pos_y: int,
                 size=20,
                 font_type=FONT,
                 color: tuple = (255, 255, 255)):

        self.text = text
        self.text_size = size
        self.text_color = color
        self.text_font = font_type
        self.text_padding = 15

        self.x = pos_x
        self.y = pos_y

        self.background = False
        self.background_color = (255, 255, 255)

        self.border = False
        self.border_color = (0, 255, 0)
        self.border_thickness = 2

    def set_text(self, new_text: str) -> None:
        self.text = new_text

    def set_font(self, new_font_type: str) -> None:
        self.text_font = new_font_type

    def set_text_color(self, new_color: tuple) -> None:
        self.text_color = new_color

    def set_text_size(self, new_size: int) -> None:
        self.text_size = new_size

    def set_text_padding(self, new_padding: int) -> None:
        self.text_padding = new_padding

    def set_position(self, new_x: int or None, new_y: int or None) -> None:
        if new_x:
            self.x = new_x
        if new_y:
            self.y = new_y

    def set_background(self, new_bool: bool) -> None:
        self.background = new_bool

    def set_background_color(self, new_color: tuple) -> None:
        self.background_color = new_color

    def set_border(self, new_bool: bool) -> None:
        self.border = new_bool

    def set_border_color(self, new_color: tuple) -> None:
        self.border_color = new_color

    def set_border_thickness(self, new_thickness: int) -> None:
        self.border_thickness = new_thickness

    def show(self, surface) -> None:

        text_surface = pygame.font.Font(self.text_font, self.text_size).render(self.text, True, self.text_color)
        text_rectangle = text_surface.get_rect(center=(self.x, self.y))

        if self.background:
            pygame.draw.rect(surface, self.background_color, text_rectangle.inflate(self.text_padding, self.text_padding))

        if self.border:
            pygame.draw.rect(surface, self.border_color,
                             text_rectangle.inflate(self.text_padding, self.text_padding), self.border_thickness)

        surface.blit(text_surface, text_rectangle)
